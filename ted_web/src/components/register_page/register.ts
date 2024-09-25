async function register(file: File, username: string, password: string, 
    first_name: string, last_name: string, email: string,sex: string,birthday: string) {
    try {
        let formData = new FormData();

        // 创建用户信息对象
        let userinfo = {
            username: username,
            password: password,
            first_name: first_name,
            last_name: last_name,
            email: email,
            sex: sex,
            birthday: birthday
        };

        // 将用户信息附加到 FormData 中
        formData.append('userinfo', JSON.stringify(userinfo));
        // 将文件附加到 FormData 中
        formData.append('file', file);

        // 发送请求
        const res = await fetch('http://127.0.0.1:8000/api/user/RegisterView/', {
            method: 'POST',
            body: formData  // 使用 FormData
        });

        const data = await res.json();
        return data;
    } catch (e) {
        console.error(e);
    }
}

export { register };
