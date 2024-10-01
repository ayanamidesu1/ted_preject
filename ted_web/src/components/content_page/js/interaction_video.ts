async function video_operation_interaction(video_id:any,operation_type:any) {
    try{
        const res=await fetch('http://localhost:8000/api/video/VideoInteraction/',{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'Authorization':'Bearer '+localStorage.getItem('auth_token')
            },
            body:JSON.stringify({
                video_id:video_id,
                interaction_type:operation_type
            })
        })
        if(res.ok){
            const data=await res.json();
            return data;
        }
        else{
            const data=await res.json();
            console.warn('交互失败')
            return data;
        }
    }
    catch (error) {
        console.log(error);
    }
}

export default video_operation_interaction;