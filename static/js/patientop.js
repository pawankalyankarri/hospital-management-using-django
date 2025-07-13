
function validatePatOp(){
    let pat_name = document.querySelector('#pn').value;
    let pat_age = document.querySelector('#pa').value;
    let pat_add = document.querySelector('#padd').value;
    let pat_mobile = document.querySelector('#pmn').value;
    let pat_amount = document.querySelector('#payment');

    if (pat_amount.checked  && pat_name.length >=3 && pat_add.length >=3 && pat_mobile.length == 10){
        console.log('ok')
        return true
    }    
    else {
        console.log('failed')
        return false
    }
    
       
    
}

