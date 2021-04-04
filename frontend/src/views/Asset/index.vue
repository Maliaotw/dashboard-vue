<template>
  <div style="min-height: 600px">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item>資產</el-breadcrumb-item>
      <el-breadcrumb-item>物理資源</el-breadcrumb-item>
    </el-breadcrumb>

    <el-row type="flex">

      <el-col :span="24" style="text-align: right">

        <el-form :model="filterform">

          <label class="ml-2">ID</label>
          <el-input
              v-model="filterform.id"
              placeholder="请输入内容"
              style="width:15%; margin-right: 20px;"
              class="ml-2 mr-2"
              @change="handleFilterSubmit"
          >

          </el-input>


          <label class="ml-2">業務線</label>
          <el-select v-model="filterform.busline"
                     class="ml-2 mr-2"
                     placeholder=""
                     @change="handleFilterSubmit"
          >
            <el-option key="" label="----" value=""/>
            <el-option v-for="item in this.buslinelist" :label="item.name" :key="item.id" :value="item.id"/>

          </el-select>

          <label class="ml-2">分類</label>
          <el-select v-model="filterform.category"
                     class="ml-2 mr-2"
                     placeholder=""
                     @change="handleFilterSubmit"
          >
            <el-option key="" label="----" value=""/>
            <el-option v-for="item in this.categorylist" :label="item.name" :key="item.id"
                       :value="item.id"/>

          </el-select>

        </el-form>

      </el-col>

    </el-row>

    <el-table
        :data="tableData"
        size="small"

    >
      <el-table-column label="ID" prop="id"/>
      <el-table-column label="分類" prop="category"/>
      <el-table-column label="業務線" prop="busline"/>
      <el-table-column label="備註" prop="remarks"/>
    </el-table>

    <el-pagination
        :page-sizes="[5,10,20,50,100]"
        :page-size="pageSize"
        :pager-count="7"
        layout="total, sizes, prev, pager, next"
        :total="total"
        @current-change="handleIndexChange"
        @size-change="handleSizeChange"
        style="float: right;margin-top: 20px"
    >
    </el-pagination>

  </div>
</template>


<script>

import {getAssetList} from '@/api/asset'

export default {
  components: {},
  data() {
    return {
      total: 0,
      pageSize: 10,
      page: 1,
      tableData: [],
      title: '',
      formLabelWidth: '120px',
      CreateisShow: false,
      dialogVisible: false,
      DeleteForm: {
        name: '',
        id: ''
      },
      filterform: {},


    }
  },
  mounted() {

  },
  methods: {
    // 提交搜索
    handleFilterSubmit() {
      this.getInit(this.page, this.pageSize, this.filterform)
    },

    // 分頁
    handleIndexChange(p) {
      this.page = p
      this.getInit(this.page, this.pageSize)

    },
    handleSizeChange(size) {
      this.page = 1
      this.pageSize = size
      this.getInit(this.page, this.pageSize)

    },
    // 請求資產
    getInit(p, size, params) {
      if (p === '1') {
        p = 0
      } else {
        p = p - 1
      }
      const page = p * this.pageSize;

      getAssetList(page, size,params)
          .then((response) => {
            // console.log(response.results)
            this.tableData = response.results;
            this.categorylist = response.category;
            this.buslinelist = response.busline;
            this.total = response.count;
          })

          // .catch((error) => {
          //   this.$notify.error({
          //     title: '错误',
          //     message: '这是一条错误的提示消息'
          //   });
          // })


    },

  },
  created() {
    this.getInit(this.page, this.pageSize)
  }


}


</script>

<style scoped>


</style>