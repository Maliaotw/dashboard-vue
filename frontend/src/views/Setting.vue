<template>

    <div style="min-height: 600px">

      <el-breadcrumb separator="/">
        <el-breadcrumb-item>Settings</el-breadcrumb-item>
      </el-breadcrumb>


      <el-row class="mt-4">


            <el-tabs v-model="activeName" type="border-card" @tab-click="handleClick">
                <el-tab-pane label="iDRAC管理" name="idrac">

                        <el-row>
                            <el-col :span="14" :offset="6">
                                <el-form
                                         :model="form"
                                         ref="idrac"
                                         label-position="left"
                                         label-width="100px"
                                         class="demo-form-inline"
                                >


                                    <el-row type="flex" :gutter="20">

                                        <el-col>

                                            <el-form-item
                                                    label="User"
                                                    prop="IDRAC_USER"
                                                    :rules="{required: true, message: 'User不能為空', trigger: 'blur'}"
                                            >

                                                <el-input v-model="form.IDRAC_USER" placeholder=""></el-input>
                                            </el-form-item>

                                        </el-col>


                                    </el-row>


                                    <el-row type="flex" :gutter="20">

                                        <el-col>

                                            <el-form-item
                                                    label="Passwd"
                                                    prop="IDRAC_PASSWD"
                                                    :rules="{required: true, message: 'Passwd不能為空', trigger: 'blur'}"
                                            >

                                                <el-input v-model="form.IDRAC_PASSWD" placeholder="" show-password></el-input>
                                            </el-form-item>

                                        </el-col>

                                    </el-row>



                                    <el-row>
                                        <el-col style="text-align: center">
                                            <el-button @click="submitForm('idrac')" type="primary">提交</el-button>
                                        </el-col>
                                    </el-row>


                                </el-form>
                            </el-col>
                        </el-row>


                </el-tab-pane>

                <el-tab-pane label="Vcenter管理" name="vcenter">

                    <el-row>
                        <el-col :span="14" :offset="6">
                            <el-form
                                    :model="form"
                                    ref="vcenter"
                                    label-position="left"
                                    label-width="180px"
                                    class="demo-form-inline"
                            >

                                <el-row type="flex" :gutter="20">

                                    <el-col>

                                        <el-form-item
                                                label="VCENTER_SERVER"
                                                prop="VCENTER_SERVER"
                                                :rules="{required: true, message: '設備名稱不能為空', trigger: 'blur'}"
                                        >

                                            <el-input v-model="form.VCENTER_SERVER" placeholder=""></el-input>
                                        </el-form-item>

                                    </el-col>


                                </el-row>


                                <el-row type="flex" :gutter="20">

                                    <el-col>

                                        <el-form-item
                                                label="VCENTER_USER"
                                                prop="VCENTER_USER"
                                                :rules="{required: true, message: 'VCENTER_USER不能為空', trigger: 'blur'}"
                                        >

                                            <el-input v-model="form.VCENTER_USER" placeholder=""></el-input>
                                        </el-form-item>

                                    </el-col>

                                </el-row>

                                <el-row type="flex" :gutter="20">

                                    <el-col>

                                        <el-form-item
                                                label="VCENTER_PASS"
                                                prop="VCENTER_PASS"
                                                :rules="{required: true, message: 'VCENTER_PASS不能為空', trigger: 'blur'}"
                                        >

                                            <el-input v-model="form.VCENTER_PASS" placeholder="" show-password></el-input>
                                        </el-form-item>

                                    </el-col>

                                </el-row>



                                <el-row>
                                    <el-col style="text-align: center">
                                        <el-button @click="submitForm('vcenter')" type="primary">提交</el-button>
                                    </el-col>
                                </el-row>


                            </el-form>
                        </el-col>
                    </el-row>



                </el-tab-pane>

            </el-tabs>

        </el-row>




    </div>

</template>


<script>

    import {getSeeingsObj,UpdateSeeingsObj} from '@/api/settings'

    export default {
        data() {
            return {
                title: '',
                formLabelWidth: '120px',
                form: {},
                activeName: 'idrac'
            }
        },

        methods: {
            handleClick(tab, event) {
                this.getInit(tab.paneName)

            },
            getInit(name){
                getSeeingsObj(name)
                    .then((response) => {
                        this.form = response;
                    })
                    .catch((error) => {
                        // this.$notify.error({
                        //     title: '错误',
                        //     message: '这是一条错误的提示消息'
                        // });
                    })
            },
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        UpdateSeeingsObj(formName,this.form)
                            .then((response) => {
                                this.$notify.success({
                                    title: '成功',
                                    message: '更新成功'
                                });
                            })
                    } else {
                        return false;
                    }
                });
            },

        },
        created() {
            // get and set auth user
            this.getInit(this.activeName)
        }


    }
</script>
