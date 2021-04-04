import http from '@/services/http'


export function getAssetList(page, size, params) {
    return http({
        url: `/api/asset/?offset=${page}&limit=${size}`,
        method: 'get',
        params
    })
}

