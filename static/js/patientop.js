function validatePatOp(e) {
  let pat_name = document.querySelector("#pn").value;
  let pat_age = document.querySelector("#pa").value;
  let pat_add = document.querySelector("#padd").value;
  let pat_mobile = document.querySelector("#pmn").value;
  let pat_amount = document.querySelector("#payment");
  let pat_gender = document.querySelector('#gender').value

//   e.preventDefault()
//   if (pat_name.length == 0){
//     document.querySelector('#pat_name_error').innerHTML = 'Please Enter valid Patient Name'
//     document.querySelector('#pn').style.borderColor = 'red'
//   }
  if (
    pat_amount.checked &&
    pat_name.length >= 3 &&
    pat_add.length >= 3 &&
    pat_mobile.length == 10 &&
    Number(pat_mobile[0]) > 5 &&
    Number(pat_age)> 0 && Number(pat_age<=100) &&
    pat_gender.length > 1
  ) {
    
    console.log("true");
    return true;
  } else {
    console.log("failed");
    return false;
  }
}
