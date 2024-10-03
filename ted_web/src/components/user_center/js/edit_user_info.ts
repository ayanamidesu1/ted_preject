async function edit_user_info(edit_type:any,username:any,user_tags:any,
    self_website:any,self_website_introduce:any):Promise<any> {
    try {
        const res = await fetch('http://localhost:8000/api/user/EditUserInfo/', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
            },
            body:JSON.stringify({
                edit_type:edit_type,
                username:username,
                user_tags:user_tags,
                self_website:self_website,
                self_website_introduce:self_website_introduce
            })
        })
        if(res.ok){
            const data=await res.json();
            return data
        }
        else{
            const data=await res.json();
            console.log('修改用户信息失败')
            return data
        }
    }
    catch(e){
        console.log(e)
    }
}
async function edit_user_password(edit_type:any,once_password:any,new_password:any,email:any){
    try {
        const res = await fetch('http://localhost:8000/api/user/EditUserInfo/', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
            },
            body:JSON.stringify({
                edit_type:'password',
                once_password:once_password,
                new_password:new_password,
                email:email
            })
        })
        if(res.ok){
            const data=await res.json();
            return data
        }
        else{
            const data=await res.json();
            console.log('修改用户密码失败')
            return data
        }
    }
    catch(e){
        console.log(e)
    }

}

async function edit_user_avatar(file: File): Promise<any> {
    try {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('edit_type', 'avatar'); // 加入 edit_type 字段

        const res = await fetch('http://localhost:8000/api/user/EditUserAvatar/', {
            method: 'post',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('auth_token')}`
            },
            body: formData
        });

        if (res.ok) {
            const data = await res.json();
            return data;
        } else {
            const data = await res.json();
            console.log('修改用户头像失败');
            return data;
        }
    } catch (e) {
        console.log(e);
    }
}

export default edit_user_info
export {edit_user_password,edit_user_info,edit_user_avatar}