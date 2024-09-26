async function get_token(username: string, password: string) {
    try {
        const res = await fetch('http://127.0.0.1:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })
        const data = await res.json()
        return data
    }
    catch (e) {
        console.log(e)
    }
}

async function verify_token(token: string) {
    try{
        const res=await fetch('http://127.0.0.1:8000/api/token/verify/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                token: token
            })
        })
        if(res.ok){
            return true
        }
        else{
            return false
        }
    }
    catch(e)
    {
        console.log(e)
    }
}

async function refresh_token(token: string) {
    try {
        const res = await fetch('http://127.0.0.1:8000/api/token/refresh/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                refresh: token
            })
        });
        const data = await res.json();
        if (data.access) {
            return data.access; // 返回新的 access token
        } else {
            console.error('Failed to refresh token', data);
            return null;
        }
    } catch (e) {
        console.log(e);
        return null;
    }
}

async function get_csrf_token() {
    try {
        const res = await fetch('http://127.0.0.1:8000/api/csrf/',)
        const data = await res.json()
        return data
    }
    catch (e) {
        console.log(e)
    }
}

export {get_token, get_csrf_token, verify_token,refresh_token}