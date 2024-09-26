declare function get_token(username: string, password: string): Promise<string>;
declare function get_csrf_token(): Promise<string>;
declare function verify_token(token: string): Promise<boolean>;
declare function refresh_token(token: string): Promise<string>;
export { get_token, get_csrf_token,verify_token,refresh_token};