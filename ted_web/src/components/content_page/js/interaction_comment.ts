async function interaction_comment(comment_id:any,interaction_type:any,comment_type:any):Promise<any>{
    try{
        const res=await fetch('http://localhost:8000/api/comment/InteractionComment/',{
            method:'post',
            headers:{
                'Content-Type':'application/json',
                'Authorization':'Bearer '+localStorage.getItem('auth_token')
            },
            body:JSON.stringify({
                comment_id:comment_id,
                interaction_type:interaction_type,
                comment_type:comment_type
            })
        })
        if(res.ok){
            const data=await res.json();
            return data;
        }
        else{
            const data=await res.json();
            console.warn('交互错误')
            return data;
        }
    }
    catch(error){
        console.log(error);
    }
}

export default interaction_comment;