
import { useState } from "react";

export default function Home(){

const [idea,setIdea] = useState("");
const [result,setResult] = useState("");

const buildProject = async ()=>{

const res = await fetch("http://localhost:8000/build",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({idea})
})

const data = await res.json()

setResult(JSON.stringify(data,null,2))

}

return (

<div style={{padding:"40px"}}>

<h1>AI Engineering Assistant</h1>

<input
value={idea}
onChange={(e)=>setIdea(e.target.value)}
placeholder="Enter startup idea"
/>

<button onClick={buildProject}>Build</button>

<pre>{result}</pre>

</div>

)

}
