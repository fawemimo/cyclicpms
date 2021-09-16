let levelform = document.querySelector('#level-form')

let leveldatabox = document.querySelector('#level-data-box')
let levelInput = document.querySelector('#levels')

// for grades 
let gradedatabox = document.querySelector('#grades-data-box')
let gradeInput = document.querySelector('#grades')

let gradeText = document.querySelector('#grade-text')

let levelText = document.querySelector('#level-text')

let btnBox = document.querySelector('#btn-box');
let alertBox = document.querySelector('#alert-box');

let csrf = document.getElementsByName('csrfmiddlewaretoken')

$.ajax({
    url:`{% url 'get_json_level_data' %}`,
    type:'GET',
    success:function(response){
        console.log(response.data)
        let levelData = response.data
        levelData.map(item => {
            let option = document.createElement('div')
            option.textContent = item.level
            option.setAttribute('class', 'item')
            option.setAttribute('data-value', item.level)
            leveldatabox.appendChild(option)
        })
    },
    error: function(error){
        console.log(error)
    }

})

levelInput.addEventListener('change',e=>{
    console.log(e.target.value)

    let selectedLevel = e.target.value
    alertBox.innerHTML = ''
    gradedatabox.innerHTML = ''
    gradeText.textContent = 'Select grade'



levelform.addEventListener('submit', e=>{
    e.preventDefault()
    console.log('submitted')

    $.ajax({
        url:`save_add_category/${selectedLevel}`,
        type:'POST',
        data:{
            'csrfmiddlewaretoken':csrf[0].value,
            'level':levelText.textContent,
            'grade':gradeText.textContent,
        },

        success: function(response){
            console.log(response)
            alertBox.innerHTML = `<div class="ui positive message">
                
                                    <div class="header">
                                        Success
                                    </div>
                                    <p>Employee categories added successfully</p>
                                </div>`
        },
        error: function(error){
            console.log(error)
            alertBox.innerHTML =`<div class="ui negative message">
                
                                    <div class="header">
                                    Failed
                                    </div>
                                    <p>Failed to add categories</p>
                                </div>`
        }
    });
})   ;
});

 