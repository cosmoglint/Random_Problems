let chuckapi= 'https://api.chucknorris.io/jokes/random'
promises=[]


// asadas
for (let i=0;i<50;i++){
  getapi()
  .then((ans)=>{
    fin = ans.replace('Chuck Norris','Suriyaaaaa')
    document.getElementById("main").innerHTML += "<br />" + fin;
  })
}
// Promise.all(promises)
// .then((ans)=>{
//   for (let i=0;i<promises.length;i++){
//     console.log(ans[i]);
//     document.getElementById("main").innerHTML += "<br />" + ans[i];


  // }
// })
async function getapi(){
  let res= await fetch(chuckapi)
  let data= await res.json()
  let value= await data.value
  return value
}


// a -> b -> c


//  Promise : isresolved, status, error
