async function get_all_user_info() {
    try{
        const res=await fetch('http://localhost:8000/api/user/GetAllUserInfo/',{
            method:'post',
            headers:{
                'Content-Type':'application/json',
                'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
            },

        })
        if(res.ok){
            const data=await res.json();
            return data
        }
        else{
            const data=await res.json();
            console.warn('获取用户信息失败')
            return data
        }
    }
    catch (error) {
        console.log(error);
    }
}
export default get_all_user_info