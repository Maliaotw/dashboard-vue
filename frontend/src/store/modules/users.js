import {getProfile, logout} from '@/api/users'
import {getCurrentOrgFromCookie, getCurrentRoleFromCookie, getTokenFromCookie, getUsernameCookie} from '@/utils/auth'
import {resetRouter} from '@/router'

const getDefaultState = () => {
    return {
        token: getTokenFromCookie(),
        username: getUsernameCookie(),
        navTags: [],
        isNavMenuOpen: true,
        isAuthenticated: false,
        active: "",
    }
}

const state = getDefaultState()

const mutations = {

    toggleMenuOpen(state, payload) {
        state.isNavMenuOpen = !state.isNavMenuOpen
    },

}

const actions = {

    updateToken(state, {newToken,}) {
        // TODO: For security purposes, take localStorage out of the project.
        localStorage.setItem('token', newToken);
        state.jwt = newToken;
        Cookies.set('token', newToken)

        // Vue.set(state, 'jwt', newToken)
    },
    removeToken(state) {
        // TODO: For security purposes, take localStorage out of the project.
        state.jwt = "";
        state.authUser = "";
        localStorage.removeItem('token');
        localStorage.removeItem('authUser');
        localStorage.removeItem('isAuthenticated');
        // state.jwt = null;

    },

    // user logout
    logout({commit, state}) {
        return new Promise((resolve, reject) => {
            logout(state.token).then(() => {
                // removeToken() // must remove  token  first
                resetRouter()
                commit('RESET_STATE')
                resolve()
            }).catch(error => {
                reject(error)
            })
        })
    },
}

export default {
    namespaced: true,
    state,
    mutations,
    actions
}
