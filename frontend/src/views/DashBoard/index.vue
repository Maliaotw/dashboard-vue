<template>
  <div>

    <el-row type="flex" class="mb-2">
      <el-col :span="6" v-for="(infor, i) in inforCardData">
        <el-card
            shadow="always"
            class="mr-1"
            :body-style="{ padding: '10px'}"
        >
          <el-row type="flex">
            <el-col
                :span="6"
                align="center"
            >
              <font-awesome-icon :icon="['fa', infor.icon]" style="font-size: 50px;margin: 10px" />
            </el-col>
            <el-col
                :span="18"
                align="right"
            >
              <p v-bind:style="{color:infor.color}">
                {{ infor.title }}
              </p>
              <p>
                {{ infor.count }}
              </p>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>

    <el-row type="flex">
            <el-col :span="16">
                <div class="mt-0"
                >
                    <line-chart
                            :chart-data="datacollection"
                    >
                    </line-chart>
                </div>
            </el-col>
            <el-col
                    :span="6"
            >
                <div class="small"
                     style="margin-left: 20px"
                >
                    <pie-chart
                            :chart-data="pie"
                    >
                    </pie-chart>
                </div>

            </el-col>


        </el-row>






  </div>
</template>


<script>

import LineChart from '../../Chart/LineChart'
import PieChart from '../../Chart/PieChart'
import {getDashBoard} from '@/api/dashboard'

export default {
  components: {
    LineChart,
    PieChart,
  },
  data() {
    return {
      datacollection: null,
      pie: null,
      data: {
        count: {
          asset: 12,
        },
      },
      inforCardData: [
        {"title": "服務器", "count": 2, "icon": "el-icon-s-fold"},
        {"title": "網路設備", "count": 2, "icon": "el-icon-s-fold"},
        {"title": "虛擬機", "count": 2, "icon": "el-icon-s-fold"},
        {"title": "總數", "count": 6, "icon": "el-icon-s-fold"},
      ],

    }
  },
  mounted() {

  },
  methods: {
            fillData() {
                this.datacollection = {
                    labels: this.data.asset_data.label,
                    datasets: [
                        {
                            label: '更新',
                            backgroundColor: '#74f81d',
                            data: this.data.asset_data.latest_data,
                            fill: false,
                            borderColor: '#74f81d',
                            // pointBackgroundColor: 'white',
                            // borderWidth: 1,
                            // pointBorderColor: 'white',
                        }, {
                            label: '創建',
                            // backgroundColor: '#f87979',
                            data: this.data.asset_data.create_data,
                            fill: false,
                            borderColor: '#f87979',
                            // pointBackgroundColor: 'white',
                            // borderWidth: 1,
                            // pointBorderColor: 'white',
                        }
                    ],
                }
            },
            pieData() {
                this.pie = {
                    hoverBackgroundColor: "red",
                    hoverBorderWidth: 10,
                    labels: this.data.asset_type.label,
                    datasets: [
                        {
                            label: this.data.asset_type.label,
                            data: this.data.asset_type.data,
                            // fill: false,
                            backgroundColor: ["#41B883", "#E46651", "#00D8FF"],
                            // pointBackgroundColor: 'white',
                            // pointBorderColor: 'white',
                        }
                    ],
                }
            },
            getDash() {
                getDashBoard()
                    .then((res) => {
                        console.log(res);
                        this.data = res
                        this.inforCardData = res.count
                        this.fillData();
                        this.pieData()
                    })

            }
        },
  created() {
    this.getDash()
    // console.log(this.data.asset_data.label)
  }


}


</script>

<style scoped>


</style>