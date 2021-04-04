<template>
  <div class="footer" :style="style">
    <div class="pull-right">
      Version <strong>1.0.0</strong> <span> GPLv2. </span>
    </div>
    <div style="padding-left:20px;">
      <strong>Copyright</strong> DemoWeb © 2021
    </div>
  </div>
</template>
<script>
import {mapState} from 'vuex'
export default {
  name: 'Footer',
  computed: {
    ...mapState(
        {
          isNavMenuOpen: state => state.users.isNavMenuOpen
        }
    ),
    style() {
      return this.isNavMenuOpen ? ('margin-left: 200px;') : ('margin-left: 64px')
    }

  },

}
</script>
<style >
.el-footer{
    padding: 0;
    height: 35px !important;
}
.pull-right {
    float: right!important;
}
.footer{
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    padding: 10px 20px;
    background: white;
    border-top: 1px solid #e7eaec;
    transition:margin-left 0.3s;
    //border-top: 1px solid #e7eaec;
    div{
        font-size: 13px;
    }
}
</style>
