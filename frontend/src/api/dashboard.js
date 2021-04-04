import http from '@/services/http'

export function getDashBoard() {
    return http({
        url: 'api/dashboard',
        method: 'get',
    })
}