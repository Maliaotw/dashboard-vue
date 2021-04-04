<template>
    <div>

        <NavMenu/>
        <div class="v3-main" :style="{'margin-left': isNavMenuOpen ? '200px': '64px'}">
            <div class="v3-header"><Header/></div>
            <el-main class="v3-content-main"><router-view/></el-main>
            <div><Footer/></div>
        </div>
    </div>
</template>
<script>
    import {mapGetters, mapState} from 'vuex'
    import NavMenu from '../components/NavMenu'
    import Header from '../components/Header'
    import Footer from '../components/Footer'

    export default {
        name: 'Base',
        components: {
            NavMenu, Header,Footer
        },
        computed: {
            ...mapState(
                {
                  isNavMenuOpen: state => state.users.isNavMenuOpen
                }
            ),
        }
    }
</script>

<style scoped>
    .v3-header {
        height: 40px;
        border-bottom: 1px solid #eee;
        background: #fff
    }

    .v3-main {
        margin-left: 200px;
    }

    .v3-content-main {
        background: #fff;
        margin: 10px;
        font-size: 14px;
        min-height: 600px;
    }

    .el-footer {
    background: white;
    border-top: 1px solid #e7eaec;
    width: 100%;
    }
</style>
