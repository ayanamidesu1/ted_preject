
async function register(
    file: File,
    username: string,
    password: string,
    first_name: string,
    last_name: string,
    email: string,
    sex: string,
    birthday: string
) {
    try {
        let formData = new FormData();
        let csrftoken = localStorage.getItem('csrftoken') as string;

        let userinfo = {
            username: username,
            password: password,
            first_name: first_name,
            last_name: last_name,
            email: email,
            sex: sex,
            birthday: birthday,
        };

        formData.append('userinfo', JSON.stringify(userinfo));
        formData.append('file', file);

        // 发送请求
        const res = await fetch('http://127.0.0.1:8000/api/user/RegisterView/', {
            method: 'POST',
            credentials: 'include', // 添加凭证
            headers: {
                'X-CSRFToken': csrftoken || '', // 添加 CSRF Token，使用空字符串作为默认值
            },
            body: formData, // 使用 FormData
        });

        if (!res.ok) {
            throw new Error(`HTTP error! status: ${res.status}`);
        }

        const data = await res.json();
        return data;
    } catch (e) {
        console.error(e);
    }
}

export { register };
