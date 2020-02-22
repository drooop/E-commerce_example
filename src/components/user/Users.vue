<template>
  <div>
    <!-- -->
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">
        首页
      </el-breadcrumb-item>
      <el-breadcrumb-item>用户管理</el-breadcrumb-item>
      <el-breadcrumb-item>用户列表</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- Card -->
    <el-card>
      <!-- 搜索与添加区域 -->
      <el-row :gutter="20">
        <el-col :span="8">
          <el-input
            placeholder="请输入内容"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
            />
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button type="primary">
            添加用户
          </el-button>
        </el-col>
      </el-row>
      <!-- 用户列表区域 -->
      <el-table
        :data="userList"
        border
        stripe
      >
        <el-table-column
          label="#"
          type="index"
        />
        <el-table-column
          label="姓名"
          prop="user_name"
        />
        <el-table-column
          label="邮箱"
          prop="email"
        />
        <el-table-column
          label="电话"
          prop="mobile"
        />
        <el-table-column
          label="角色"
          prop="role_name"
        />
        <el-table-column
          label="状态"
          prop="mg_state"
        >
          <template v-slot="scope">
            <el-switch
              v-model="scope.row.mg_state"
            />
          </template>
        </el-table-column>
        <el-table-column
          label="操作"
        >
          <template v-slot="scope">
            <!-- 修改按钮 -->

            <el-button
              type="primary"
              icon="el-icon-edit"
              size="mini"
            />

            <!-- 删除按钮 -->
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
            />

            <el-tooltip
              class="item"
              effect="dark"
              content="分配角色"
              placement="top"
              :enterable="false"
              :hide-after="800"
            >
              <!-- 分配角色按钮 -->
              <el-button
                type="warning"
                icon="el-icon-setting"
                size="mini"
              />
            </el-tooltip>
          </template>
        </el-table-column>
      </el-table>
      <!-- 分页 -->
      <el-pagination
        :current-page="queryInfo.pagenum"
        :page-sizes="[1, 2, 5, 10]"
        :page-size="queryInfo.pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      />
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // 获取用户列表的参数对象
      queryInfo: {
        query: '',
        // 当前页码
        pagenum: 1,
        // 当前显示条目数
        pagesize: 1
      },
      userList: [],
      total: 0
    }
  },
  created () {
    this.getUserList()
  },
  methods: {
    async getUserList () {
      const { data: res } = await this.$http.get('users', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        return this.$message.error('获取用户列表失败')
      }
      this.userList = res.data.users
      this.total = res.data.total
      console.log(res)
    },
    // 监听 pagesize 改变事件, 传递将要更新到的显示条目数
    handleSizeChange (newSize) {
      console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getUserList()
    },
    // 监听 page 改变事件, 传递将要更新到的页码数
    handleCurrentChange (newPage) {
      console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getUserList()
    }
  }
}
</script>

<style lang="less" scoped>

</style>
