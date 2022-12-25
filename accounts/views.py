from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import CreateView, FormView
from accounts.utils import send_sms
from confidentials.forms import *
from confidentials.models import *
from managements.forms import *
from managements.models import *
from .forms import LoginForm, OtpCodeForm, UserConfirmForm
from django.views.decorators.csrf import csrf_exempt

# API's import
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet # for custom filter search
from django_filters import rest_framework as filters
from rest_framework.parsers import FormParser,MultiPartParser,JSONParser, FileUploadParser


class UserCustomFilter(FilterSet):
    is_active = filters.CharFilter('is_active')
    user_type = filters.CharFilter(method='filter_by_user_type')
    class Meta:
        model = User
        fields = ('is_active', 'user_type')

    def filter_by_user_type(self, queryset, name, value) :
        queryset = User.objects.filter(user_type__exact=value)   
        return queryset  



class UserFilterListView(viewsets.ModelViewSet):

    """
    USER FILTER
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    # filter_fields = ('is_active', )
    filter_class = UserCustomFilter
    ordering_fields = ('is_active', 'username')
    ordering = ('username')
    search_fields = ('first_name','username')


    @action(detail=True, methods=['put'])
    def profile_pics(self, request, pk=None):
        user  = self.get_object()
        employee = user.employee
        serializer  = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)    

    # def get_queryset(self):
    #     queryset = User.objects.all()
    #     active = self.request.query_params.get("is_active", "")
    #     if active:
    #         if active == "False":
    #             active = False
    #         elif active == "True":
    #             active = True
    #         else:
    #             return queryset
    #         return queryset.filter(is_active=active)
    #     return queryset


class UploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(seelf, request):
        file = request.data.get('file',  None)
        import pdb; pdb.set_trace()
        print(file)
        if file:
            return Response({'message':'Photo uploaded successfully'}, status=200)
        else:
            return Response({'message':'photo declined'}, status=400)    

class LoginView(APIView):
  
    """API LOGIN VIEW"""

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutAPIView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        logout(request)
        return Response(status=200)


class UserGenericView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, id):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

    def perform_create(self, serializer):
        serializer.save()


class UserAPIView(APIView):
    """
    CLASS BASED APIView
    """

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class UserDetailAPIView(APIView):
    """
    CLASS BASED APIVIEW FOR DETAILS
    """

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist as e:
            return Response({"error": "User not found"}, status=400)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serializer = UserSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = UserSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return HttpResponse(status=204)


class UserViewSet(viewsets.ModelViewSet):
    """
    USER API VIEWSETS
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


# from rest_framework.request import Request 
# class UserViewSet(viewsets.ViewSet):
#     """
#     SECOND APPROACH TO THE MODELVIEWSET
#     """
    
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer_class = UserSerializer(queryset, many=True)
#         # serializer_context = {
#         # 'request':Request(request)
#         # } 
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer_class = UserSerializer(user)

#         # serializer_context = {
#         # 'request':Request(request)
#         # } 
#         return Response(serializer_class.data)


@csrf_exempt
def all_user_view(request):
    """
    FUNCTIONS BASED VIEW API's
    """
    if request.method == "GET":
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def single_user_details_view(request, id):
    """
    FUNCTION BASED VIEW     API
    """
    try:
        instance = User.objects.get(id=id)
    except User.DoesNotExist as e:
        return JsonResponse({"error": "User not found."}, status=404)

    if request.method == "GET":
        serializer = UserSerializer(instance)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = UserSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        instance.delete()
        return HttpResponse(status=204)


def login_page(request):
    form = LoginForm(request.POST or None)
    confirm = UserConfirmForm(request.POST or None)
    context = {"form": form, "confirm": confirm}
    next_ = request.GET.get("next")
    next_post = request.POST.get("next")
    redirect_path = next_ or next_post or None

    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        # recaptcha
        # recaptcha_token         = request.POST.get('g-recaptcha-response')
        # cap_url                 = 'https://www.google.com/recaptcha/api/siteverify'
        # cap_secret              = config('cap_secret')
        # cap_data                = {'secret':cap_secret,'response':recaptcha_token}
        # cap_server_response     = requests.post(url=cap_url,data=cap_data)
        # cap_json                = json.loads(cap_server_response.text)

        # if cap_json['success'] == False:
        #     messages.error(request,'Invalid Captcha Try again')
        #     return redirect('accounts-login')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            request.session["pk"] = user.pk
            login(request, user)
            try:
                del request.session["email"]
            except:
                pass
                # if request(redirect_path, request.get_host()):

                #     return redirect(redirect_path)

                messages.success(request, "Enter OTP code sent to your phone")
                if user.user_type == 5:
                    return redirect("directors")
                elif user.user_type == 1:
                    return redirect("employee")
                elif user.user_type == 2:
                    return redirect("admin")

        else:
            messages.error(request, "Input OTP code sent to your phone")
            # return redirect(redirect_path)
    return render(request, "accounts/login.html", context)


# Authentication and verification of users through OTPCODES
@login_required
def verify_view(request):
    form = OtpCodeForm(request.POST or None)
    # geting bank form first
    personalform = PersonalInfoForm(request.POST or None)

    pk = request.session.get("pk")

    if pk:

        user = User.objects.get(pk=pk)
        otpcode = user.otpcode
        otp_user = f"{user.email}: {user.otpcode}"

        if not request.POST:
            # sending sms
            #
            print(otp_user)
            # send_sms(otp_user,user.phone_number)

        if form.is_valid():

            num = form.cleaned_data.get("otp")

            if str(otpcode) == num:

                otpcode.save()

                login(request, user)
                if request.user.user_type == 1:

                    # form validations for dashboard
                    # if personalform.is_valid():
                    #     parmanent_address_verify = personalform.cleaned_data.get('parmanent_address_verify')
                    #     if parmanent_address_verify == 1:
                    #         messages.success(request, 'You have been approved')
                    #         print('go to home')
                    #     else:
                    #         messages.error(request,'You have not been approved')
                    messages.success(request, "You have successfully login")
                    return redirect("accounts-login")

                elif request.user.user_type == 2:
                    # form validations for dashboard

                    if personalform.is_valid():
                        parmanent_address_verify = personalform.cleaned_data.get("parmanent_address_verify")
                        try:
                            if parmanent_address_verify == 1:
                                messages.success(request, "You have been approved")
                                print("go to home")
                                return HttpResponse("True")
                            else:
                                messages.error(request, "You have not been approved")
                        except:
                            print("fail")
                    messages.success(request, "You have successfully login")
                    return redirect("home")

                elif request.user.user_type == 5:
                    # form validations for dashboard
                    messages.success(request, "You have successfully login")
                    return redirect("home")
                else:
                    messages.error(request, "Invalid login crendentials")

            else:
                messages.error(request, "Provide a valid OTP code")
                return redirect("accounts-login")

    context = {
        "form": form,
    }

    return render(request, "accounts/verify_login.html", context)


# Logout views


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You are now logged out.")
    return redirect("accounts-verify")


# for users to update their profile pics

# def profile(request):
#     profile = Profile.objects.get(user=request.user.id)
#     if request.method == 'POST':
#         form      = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             image       = request.FILES['image']
#             fs          = FileSystemStorage()
#             filename    = fs.save(image.name,image)
#             image_url   = fs.url(filename)
#             form.save()
#             # user dashboard
#             return redirect('')

#     else:
#         form      = ProfileUpdateForm(instance=request.user.profile)

#     context = {

#         'form':form,
#         'profile':profile

#     }
#     return render(request,'accounts/profile.html',context)


# def add_student_save(request):
#     if request.method!="POST":
#         return HttpResponse("Method Not Allowed")
#     else:
#         form=AddStudentForm(request.POST,request.FILES)
#         if form.is_valid():
#             first_name=form.cleaned_data["first_name"]
#             last_name=form.cleaned_data["last_name"]
#             username=form.cleaned_data["username"]
#             email=form.cleaned_data["email"]
#             password=form.cleaned_data["password"]
#             address=form.cleaned_data["address"]
#             session_year_id=form.cleaned_data["session_year_id"]
#             course_id=form.cleaned_data["course"]
#             sex=form.cleaned_data["sex"]

#             profile_pic=request.FILES['profile_pic']
#             fs=FileSystemStorage()
#             filename=fs.save(profile_pic.name,profile_pic)
#             profile_pic_url=fs.u���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������
