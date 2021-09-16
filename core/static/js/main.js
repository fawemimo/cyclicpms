console.log('Hello World')

let postsBox = document.querySelector('#posts-box')
let spinnerBox = document.querySelector('#spinner-box')
let loadBtn = document.querySelector('#load-btn')
let loafBox = document.querySelector('#loading-box')
let visible = 3

let handleGetData = () => {
    $.ajax({
        type: 'GET',
        url: '/posts-json/',
        success: function(response){
            console.log(response.max)

            max_size = response.max
            let data = response.data
            spinnerBox.classList.remove('not-visible')
            setTimeout(()=>{
                spinnerBox.classList.add('not-visible')
                data.map(post=>{
                    console.log(post.id)
                    postsBox.innerHTML += `<div class="inputBox">
                                                ${ education }
                                            </div>`
                })
                if(max_size){
                    console.log('done')
                    loadBox.innerHTML = '<h4> no more posts</h4>'
                }

            }, 500)
            
         
        },
        error: function(error){
            console.log(error)
        }
    })

}

handleGetData()

loadBtn.addEventListener('click', ()=>{
    visible += 3
    handleGetData()
})