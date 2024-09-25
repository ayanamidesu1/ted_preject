declare function register(file: File, username: string, password: string, 
    first_name: string, last_name: string, email: string,sex: string,birthday: string) : Promise<void>;

export {register}