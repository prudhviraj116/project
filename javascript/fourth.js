/*let buttons = document.querySelectorAll('.btn');
for (let b of buttons){
    b.addEventListener('click', process);
}
function process(event){
    let v1,v2,output,res;
    v1=parseInt(document.getElementById('t1').value);
    v2=parseInt(document.getElementById('t2').value);
    if(event.target.value=='Addition'){
        res=v1+v2;
    }
    else if(event.target.value=='Subtract'){
        res=v2-v1;
    }
    else if(event.target.value=='Multiply'){
        res=v1*v2;
    }
    else if(event.target.value=='Divide'){
        res=v1/v2;
    }
    output=document.getElementById('output');
    //output.innerText=res;
    output.innerHTML='<h2>'+event.target.value+'is'+res+'</h2>';
    output.style.color='red';
}*/ 
/*let button=document.querySelector('#btn');
button.addEventListener('click',process);
function process(event){
    let v1,v2,action,res,output;
    v1=parseInt(document.getElementById('t1').value);
    v2=parseInt(document.getElementById('t2').value);
    action=document.getElementById('action').value;
   // console.log(v1,v2,action);
   if(action=='add'){
      res=v1+v2;
   }
    else if(action=='sub'){
        res=v2-v1;
     }
    else if(action=='mul'){
        res=v1*v2;
    }
    else if(action=='div'){
        res=v1/v2;
}
output=document.getElementById('output');
output.innerHTML='<h1>'+action+'is'+res+'</h1>'
}*/
/*let button=document.getElementById('btn');
    button.addEventListener('click',process);
function process(event){
        let Fruits,output='';
        Fruits=document.querySelectorAll('.Fruits');
        for(let chkbox of Fruits){
            if(chkbox.checked==true){
                output=output+chkbox.value+' ';
            }
        }
        document.getElementById('output').innerText=output;
    }*/
    /*let chkbox = document.getElementById('chk');
    chkbox.addEventListener('click', copyAddress);
    function copyAddress(event){
        let present;
        present=document.getElementById('present').value;
        document.getElementById('permanent').value=present;
    }*/
    /*let t1 = document.getElementById('present');
    t1.addEventListener('change',copyaddress);
    function copyaddress(event){
       document.getElementById('permanent').value=event.target.value;
    }*/
/*let element;
element=document.createElement('h1');
element.innerText='we are learning js';
document.body.appendChild(element);*/
/*let button;
button=document.getElementById('btn');
button.addEventListener('click',additems);
button.addEventListener('mouseover',changecolor);
button.addEventListener('mouseleave',()=>button.style.backgroundColor='yellow');
function additems(event){
    let element,content;
    element=document.createElement('li');
    //content=document.createTextNode(event.target.value);
    element.innerText=document.getElementById('t1').value;
    element.setAttribute('style','color:red');
    document.getElementById('list').appendChild(element);
}

function changecolor(event){
    button.style.backgroundColor='blue';
}*/
