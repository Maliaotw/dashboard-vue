import http from '@/services/http'

export function getSeeingsObj(name) {
    return http({
        url: `/api/settings/${name}`,
        method: 'get',
    })
}


export function UpdateSeeingsObj(name, data) {
    return http({
        url: `/api/settings/${name}`,
        method: 'post',
        data
    })
}
