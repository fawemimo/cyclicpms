const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const progress = document.getElementById("progress");
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-step");

let formStepsNum = 0;

nextBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum++;
    updateFormSteps();
    updateProgressbar();
  });
});

prevBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum--;
    updateFormSteps();
    updateProgressbar();
  });
});

function updateFormSteps() {
  formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  formSteps[formStepsNum].classList.add("form-step-active");
}

function updateProgressbar() {
  progressSteps.forEach((progressStep, idx) => {
    if (idx < formStepsNum + 1) {
      progressStep.classList.add("progress-step-active");
    } else {
      progressStep.classList.remove("progress-step-active");
    }
  });

  const progressActive = document.querySelectorAll(".progress-step-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";
}

function btn_remove(parentDiv, beneficiaryTableDiv){
  var child = document.getElementById(beneficiaryTableDiv);
  var parent = document.getElementById(parentDiv);
  parent.removeChild(child);
}

  // $(document).ready(function () {
  //   $("#addBeneficiarybtn").click(function() {
  //     var newElement = '<div class="third-layer">\
  //     <div class="row">\
  //       <div class="col-25"> \
  //         <label for="">Full Name</label> </div>\
  //       <div class="col-75">\
  //         <input class="bene-detail" id="beneFullName" type="text" name="beneFullName[]" value=""></div> </div>'+
  //     '<div class="row">\
  //       <div class="col-25">\
  //         <label for="">Address</label> </div>\
  //       <div class="col-75">\
  //         <input class="bene-detail" id="beneAddress" type="text" name="beneAddress[]" value=""></div></div></div>'+
  //   '<div class="forth-layer">\
  //     <div class="row">\
  //       <div class="col-25">\
  //         <label for="">id_leave_reason</label> </div>\
  //       <div class="col-75">\
  //         <input class="bene-info" id="beneid_leave_reason"  name="beneid_leave_reason[]" value=""></div></div>'+
  //     '<div class="row">\
  //       <div class="col-25">\
  //         <label for="">Email</label></div>\
  //       <div class="col-75">\
  //         <input class="bene-info" id="beneEmail" name="beneEmail[]" value=""> </div></div>'+
  //      '<div class="row">\
  //       <div class="col-25">\
  //         <label for="">Value or(%)</label></div>\
  //       <div class="col-75">\
  //         <input class="bene-info" id="beneValue" name="beneEmail[]" value=""></div> </div></div></div>';
  //     $( "#beneficiaryTable" ).append( $(newElement) );
  //   });
  // });
 
    
 


  // SECOND STEP  (personal Information)


  
 var btnDisplay = document.querySelector(".btn-display");
 var leave_start = document.querySelector(".leave_start");
 var personSurname = document.querySelector(".personSurname");
 var personFirstName = document.querySelector(".personFirstName");
 var personOtherName = document.querySelector(".personOtherName");


 

// deactivate()

// function activate() { 
//   btnDisplay.disabled = false;
//   btnDisplay.style.cursor =  "pointer";

// }
// function deactivate() {
//   btnDisplay.disabled = true;
//   btnDisplay.style.cursor =  "not-allowed";
 

// }



// function check() { 
//   if(leave_start.value != '' && personSurname.value != '' &&  personFirstName.value != '' && personOtherName.value != '') { 
//     activate()
//   } else { 
//     deactivate();
//   }
// }
// leave_start.addEventListener('input', check)
// personSurname.addEventListener('input', check)
// personFirstName.addEventListener('input', check)
// personOtherName.addEventListener('input', check)




// Third step {Name of Spouse $ Beneficiary}

var btnDisplay2 = document.querySelector(".btn-display2");
var  leave_end = document.querySelector(".leave_end");
var spouseAddress = document.querySelector(".spouseAddress");
var noOfDependents = document.querySelector(".noOfDependents");
var nameOfDependents = document.querySelector(".nameOfDependents");
var beneFullName = document.querySelector(".beneFullName");
var beneAddress = document.querySelector(".beneAddress");
var beneid_leave_reason = document.querySelector(".beneid_leave_reason");
var beneEmail = document.querySelector(".beneEmail");
var beneValue= document.querySelector(".beneValue");


// deactivate2()

// function activate2() { 
//   btnDisplay2.disabled = false;
//   btnDisplay2.style.cursor = "pointer";

// }
// function deactivate2() {
//   btnDisplay2.disabled = true;
//   btnDisplay2.style.cursor =  "not-allowed";


// }

// function check2() { 
//  if( leave_end.value != '' && spouseAddress.value != '' && noOfDependents.value != '' && nameOfDependents.value != '' && beneFullName != '' && beneAddress != '' && beneid_leave_reason != '' && beneEmail != '' && beneValue != '') { 
//    activate2()
//  } else { 
//    deactivate2();
//  }
// }

// leave_end.addEventListener('input', check2)
// spouseAddress.addEventListener('input', check2)
// noOfDependents.addEventListener('input', check2)
// nameOfDependents.addEventListener('input', check2)
// beneFullName.addEventListener('input', check2)
// beneAddress.addEventListener('input', check2)
// beneid_leave_reason.addEventListener('input', check2)
// beneEmail.addEventListener('input', check2)
// beneValue.addEventListener('input', check2)





// FOURTH STEP (Asset Detail)
const btnDisplay3 = document.querySelector(".btn-display3");
const leave_reason = document.querySelector(".leave_reason");
const bankRsaNumber = document.querySelector(".bankRsaNumber");
const person_bankname = document.querySelector(".person_bankname");
const bankAccountNumber = document.querySelector(".bankAccountNumber");
const bankBranch = document.querySelector(".bankBranch");


deactivate3()

// function activate3() { 
//  btnDisplay3.disabled = false;
//  btnDisplay3.style.cursor = "pointer";



// }
// function deactivate3() {
//  btnDisplay3.disabled= true;
//  btnDisplay3.style.cursor = "not-allowed";


// }

// function check3() { 
//  if(leave_reason.value != '' && bankRsaNumber.value != '' && person_bankname.value != '' && bankAccountNumber.value != '' && bankBranch.value != '') { 
//    activate3()
//  } else { 
//    deactivate3();
//  }
// }

// leave_reason.addEventListener('input', check3)
// bankRsaNumber.addEventListener('input', check3)
// person_bankname.addEventListener('select', check3)
// bankAccountNumber.addEventListener('input', check3)
// bankBranch.addEventListener('input', check3)
