import VueCookie from 'vue-cookie'

const TOKEN_KEY = 'csrftoken'

export function getTokenFromCookie() {
    return VueCookie.get(TOKEN_KEY)
}

export function getUsernameCookie() {
    return VueCookie.get('username')
}

export function getCurrentOrgFromCookie() {
    let org = null
    try {
        org = JSON.parse(VueCookie.get(CURRENT_ORG_KEY))
    } catch (e) {
        console.log('Current org in cookie: ', org)
    }
    return org
}

