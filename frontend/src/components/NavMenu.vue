<template>
    <el-row class="tac">
        <el-col :span="24" class="h100">
            <el-menu
                    class="no-boarder el-menu-vertical-demo h100"
                    router
                    unique-opened
                    background-color="#545c64"
                    text-color="#fff"
                    :default-active="activeTag"
                    ref="mySidemenu"
                    :collapse="!isNavMenuOpen"
                    active-text-color="#ffd04b"
                    mode="vertical"
            >

                <el-menu-item style="text-align: center">Demo</el-menu-item>

                <el-menu-item index="/Home">
                    <i class="el-icon-box"/>
                    <span class="ml-2">儀表盤</span>
                </el-menu-item>


                <el-menu-item index="/Home/asset">
                    <i class="el-icon-bank-card"/>
                    <span class="ml-2">物理資源</span>
                </el-menu-item>

                <el-menu-item index="/Home/audit">
                    <i class="el-icon-menu"/>
                    <span class="ml-2">日誌審計</span>
                </el-menu-item>

                <el-menu-item index="/Home/settings">
                    <i class="el-icon-setting"/>
                    <span class="ml-2">Seetings</span>
                </el-menu-item>


            </el-menu>
        </el-col>
    </el-row>
</template>

<style scoped>
    .h100 {
        height: 100%
    }

    .tac {
        position: fixed;
        top: 0px;
        bottom: 0px;
        z-index: 999;
    }

    .el-menu-vertical-demo:not(.el-menu--collapse) {
        width: 201px;
    }
</style>

<script>
    import {mapGetters, mapState} from 'vuex'
    // import menu from '../config/menu-config'


    export default {
        data() {
            return {
                activeTag: this.activeTag,
            }
        },
        computed: {
          ...mapState(
                {
                  isNavMenuOpen: state => state.users.isNavMenuOpen
                }
          ),

        },
        methods: {
            handleOpen(key, keyPath) {
                // 選單展開
                console.log(key, keyPath)
            },
            handleClose(key, keyPath) {
                // 選單
                console.log(key, keyPath)
            }
        },
        mounted () {
            console.log('mounted')
        },
        created() {
            this.activeTag = this.$route.path
        }
    }
</script>
