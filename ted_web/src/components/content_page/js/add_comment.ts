async function add_comment(comment_id:any,content:any,comment_type:any,video_id:any):Promise<void>{
    try{
        const res=await fetch('http://localhost:8000/api/comment/AddComment/',{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'Authorization':`Bearer ${localStorage.getItem('auth_token')}`
            },
            body:JSON.stringify({
                comment_id:comment_id,
                comment_content:content,
                comment_type:comment_type,
                video_id:video_id
            })
        })
        if(res.ok){
            const data=await res.json()
            return data
        }
        else{
            console.warn('新增评论失败')
            const data=await res.json()
            return data
        }
    }
    catch(e)
    {
        console.log(e)
    }
}

export {add_comment}