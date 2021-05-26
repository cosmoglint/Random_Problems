import React from 'react';

function Test(){

    let lst = ["hi","helo","wtf"]

    let filtered_list = lst.map((data) => {return data.toUpperCase()})

    let res = filtered_list.map(
        data => <Module name={data}/>
    )

    return(
        <div>
            {res}
        </div>   
    )
}


function Module({name}){
    return(
        <p>{name}</p>
    )
}

export default Test