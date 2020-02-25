<template>
  <el-container class="home-container">
    <!-- -->
    <!-- 头部区域 -->
    <el-header>
      <div>
        <img
          src="@/assets/yhl_lr.png"
          alt=""
        >
        <span>
          云海流智能产线控制平台
        </span>
      </div>
      <el-button
        type="info"
        @click="logout"
      >
        退出
      </el-button>
    </el-header>

    <!-- 页面主体区域-->
    <el-container>
      <!-- 侧边栏 -->
      <el-aside :width="isCollapse ? '64px' : '200px'">
        <div
          class="toggle-button"
          @click="toggleCollapse"
        >
          |||
        </div>
        <!-- 侧边栏菜单区 -->
        <el-menu
          background-color="#333744"
          text-color="#fff"
          active-text-color="#409EFF"
          unique-opened
          :collapse="isCollapse"
          :collapse-transition="false"
          router
          :default-active="activePath"
        >
          <!-- 一级菜单 -->
          <el-submenu
            v-for="item of menuList"
            :key="item.id"
            :index="item.id + ''"
          >
            <!-- 一级菜单模板区 -->
            <template slot="title">
              <!-- icon -->
              <i :class="iconObj[item.id]" />
              <!-- 文本 -->
              <span>{{ item.authName }}</span>
            </template>

            <!-- 二级菜单 -->
            <el-menu-item
              v-for="subItem of item.children"
              :key="subItem.id"
              :index="'/' + subItem.path"
              @click="saveNavState('/' + subItem.path)"
            >
              <template slot="title">
                <!-- icon -->
                <i class="el-icon-menu" />
                <!-- 文本 -->
                <span>{{ subItem.authName }}</span>
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!-- 右侧内容主体 -->
      <el-main>
        <!-- 路由占位符 -->
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      // 左侧菜单数据
      menuList: [],

      iconObj: {
        1: 'el-icon-user',
        2: 'el-icon-unlock',
        3: 'el-icon-goods',
        4: 'el-icon-tickets',
        5: 'el-icon-data-line'
      },
      // 是否被折叠
      isCollapse: false,
      // 被激活的subItem链接地址
      activePath: ''
    }
  },
  created () {
    this.getMunuList()
    this.activePath = window.sessionStorage.getItem('activePath')
  },
  methods: {
    logout () {
      window.sessionStorage.clear()
      this.$router.push('/login')
    },
    async getMunuList () {
      const { data: res } = await this.$http.get('menus')
      if (res.meta.status !== 200) { return this.$message.error(res.meta.msg) }
      this.menuList = res.data
      // console.log(res)
    },
    toggleCollapse () {
      this.isCollapse = !this.isCollapse
    },
    saveNavState (activePath) {
      window.sessionStorage.setItem('activePath', activePath)
      this.activePath = activePath
    }
  }
}
</script>

<style lang="less" scoped>
.home-container {
  height: 100%;
  width:100%;
}

.el-header {
  background-color: #373d41;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items:center;
  color: #fff;
  font-size: 20px;
  > div {
    display:flex;
    align-items:center;
    span {
      margin-left: 20px;
    }
  }
}

.el-aside {
  background-color: #333744;
  .el-menu {
    border-right: none;
  }
}

.el-main {
  background-color: #eaedf1;
}

.toggle-button {
  background-color: #4A5064;
  font-size: 10px;
  line-height: 24px;
  color: #fff;
  text-align: center;
  letter-spacing: .2rem;
  cursor: pointer;
}
</style>
