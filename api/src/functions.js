const {app}=require('@azure/functions');
const {DefaultAzureCredential}=require('@azure/identity');
const {validate,endpoint,messages}=require('./core');
const credential=new DefaultAzureCredential();
app.http('chat',{methods:['POST','OPTIONS'],authLevel:'function',route:'chat',handler:async req=>{
 const origin=req.headers.get('origin');const allowed=(process.env.ALLOWED_ORIGINS||'').split(',').map(s=>s.trim()).filter(Boolean);
 const headers={'Cache-Control':'no-store','Vary':'Origin'};
 const reply=(status,body)=>({status,headers,jsonBody:body});
 if(!origin||!allowed.includes(origin))return reply(403,{error:'This course address is not enabled.'});
 Object.assign(headers,{'Access-Control-Allow-Origin':origin,'Access-Control-Allow-Methods':'POST, OPTIONS','Access-Control-Allow-Headers':'Content-Type'});
 if(req.method==='OPTIONS')return {status:204,headers};
 if(process.env.TUTOR_ENABLED!=='true')return reply(503,{error:'The Azure tutor is not enabled yet.'});
 let body;try{const raw=await req.text();if(raw.length>32000)return reply(413,{error:'Please send a shorter question.'});body=validate(JSON.parse(raw))}catch{return reply(400,{error:'Choose a section and enter a short question.'})}
 try{
 const url=endpoint(process.env.AZURE_OPENAI_ENDPOINT),deployment=process.env.AZURE_OPENAI_DEPLOYMENT;if(!deployment)throw Error('Not configured');
 const token=await credential.getToken('https://cognitiveservices.azure.com/.default');
 const r=await fetch(url,{method:'POST',headers:{Authorization:'Bearer '+token.token,'Content-Type':'application/json'},body:JSON.stringify({model:deployment,messages:messages(body),max_completion_tokens:600,store:false}),signal:AbortSignal.timeout(35000)});
 if(!r.ok)return reply(r.status===429?429:502,{error:r.status===429?'The tutor is busy. Try again shortly.':'The tutor cannot answer right now. Please ask your teacher.'});
 const data=await r.json(),text=data.choices?.[0]?.message?.content;
 return reply(200,{reply:typeof text==='string'&&text.trim()?text:'Please rephrase your computing question or ask your teacher.'});
 }catch{return reply(503,{error:'The Azure tutor is unavailable. Your workbook still works.'})}
}});
