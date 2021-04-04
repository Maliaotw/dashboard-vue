import http from '@/services/http'


export function get_loginlog(page=0,size,params) {
    return http({
        url: `/api/loginlog/?offset=${page}&limit=${size}`,
        method: 'get',
        params
    })
}
