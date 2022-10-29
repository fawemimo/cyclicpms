console.log('AJAX FORM SUBMISSIONS');
let leaveApplyForm = document.querySelector('#leave_apply_form');
let crsfToken = document.getElementsByName('csrfmiddlewaretoken');
let alertBox = document.querySelector('.alertBox');
console.log(leaveApplyForm);
console.log(crsfToken);

let leaveStart = document.querySelector('#leave_start');
let leaveEnd = document.querySelector('#leave_end');
let leaveReason = document.querySelector('#leave_reason');
 
// image display//
// let image =""
let url = ""
// image.addEventListener('change', imageChange,false);
// function imageChange(e) {
//     e.preventDefault();
//     let img_data = image.files[0];
//     let url = URL.createObjectURL(img_data);
//     console.log(url);
// imgBox.innerHTML = `<image src="${url}" width="100%">`
// }
let handleAlerts = (type, text)  => {
    alertBox.innerHtml=`<div class="alert alert-${type}" role="alert">
        ${text}
    </div>`
}

leaveApplyForm.addEventListener('submit',applyLeave,false);

function applyLeave(e) {
    e.preventDefault();

    let fd =new FormData();
    fd.append('csrfmiddlewaretoken', crsfToken[0].value)
    fd.append('leave_start', leaveStart.value);
    fd.append('leave_end', leaveEnd.value);
    fd.append('leave_reason', leaveReason.value);

    $.ajax({
        type: 'POST',
        url: url,
        data:fd,
        success: function(response){
            console.log(response);
            handleAlerts('success','Successfully applied for Leave...')
            setTimeout(()=>{
                alertBox.innerHTML="";
            }, 2000)
        },
        error: function(error){
            console.log(error)  
            handleAlerts('danger','Failed to apply for leave....');
        },
        cache: false,
        contentType: false,
        processData: false
    })

}