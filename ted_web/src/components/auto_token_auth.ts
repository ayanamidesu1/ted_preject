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

export {get_token}