declare function get_token(username: string, password: string): Promise<string>;
declare function get_csrf_token(): Promise<string>;
export { get_token, get_csrf_token};