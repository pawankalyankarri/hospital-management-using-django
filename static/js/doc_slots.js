
function validateDisease(e){
     e.preventDefault()
    document.querySelectorAll('.disease').forEach((btn)=>{
        btn.classList.remove('btn-info')
        btn.classList.add('btn-outline-info')
    })
    e.target.classList.remove('btn-outline-info')
    // console.log(e)
    e.target.classList.add('btn-info')
    document.querySelector('#dis_input').value = e.target.innerHTML
}

function validateDate(e){
    e.preventDefault()
    document.querySelectorAll('.slot').forEach((btn)=>{
        btn.classList.remove('btn-primary')
        btn.classList.add('btn-outline-primary')
    })
    e.target.classList.remove('btn-outline-primary')
    e.target.classList.add('btn-primary')
    // console.log(e)
    document.querySelector('#slot_input').value = e.target.innerHTML
}