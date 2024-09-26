async function get_userinfo(): Promise<any> {
    try{
        const res=await fetch('http://localhost:8000/api/user/GetUserInfo/',{
            method:'post',
            headers:{
                'Content-Type':'application/json',
                'Authorization':'Bearer '+localStorage.getItem('auth_token')
            },
        })
        const data=await res.json()
        return data
    }
    catch(e)
    {
        console.log(e)
    }
}
export {get_userinfo}