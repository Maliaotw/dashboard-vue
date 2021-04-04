import http from '@/services/http'

export function getHealthz() {
    return http({
        url: '/api/healthz',
        method: 'get'
    })
}

