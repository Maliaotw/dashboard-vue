<template>
    <el-container>
        <el-header></el-header>
        <el-main class="main">
            <h1>後台</h1>
            <el-form ref="form" :model="form" class="z-depth-2">
                <el-form-item>
                    <el-input v-model="form.username" placeholder="email"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-input v-model="form.password" placeholder="password" type="password"></el-input>
                </el-form-item>
                <el-form-item style="text-align:right;">
                    <el-button type="primary" @click="login">登录</el-button>
                </el-form-item>
            </el-form>
        </el-main>
        <el-footer></el-footer>
    </el-container>
</template>

<script>
    import VueCookie from 'vue-cookie'
    import store from '@/store'


    export default {
        name: 'Login',
        data() {
            return {
                form: {
                    username: 'admin',
                    password: 'admin'
                }
            }
        },
        methods: {
            reloadPage() {
                window.location.reload()
            },
            login() {
                const payload = {
                    username: this.form.username,
                    password: this.form.password
                }
                self = this
                this.$axios.post("/api/api-token-auth/", payload)
                    .then((result) => {
                        console.log(result.data)
                        VueCookie.set('csrftoken', result.data.token, 14)
                        VueCookie.set('username', result.data.username, 14)
                        self.reloadPage()
                    })
                    .catch((error) => {

                        this.$message({
                          showClose: true,
                          message: '帳號或密碼錯',
                          type: 'error'
                        });

                    })


            },

        },
        created() {
            if (this.token) {
                this.$router.push({name: 'Home'})

            }
        },
        computed: {
          token(){
              // return store.getters.token
              return VueCookie.get("csrftoken")
          },
        }

    }
</script>

<style scoped>
    h1 {
        text-align: center;
        color: #606266;
    }

    form {
        padding: 20px;
        background: #fff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
        border-radius: 2px;
    }

    .main {
        width: 400px;
        margin: 0px auto;
    }
</style>
