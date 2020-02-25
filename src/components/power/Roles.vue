<template>
  <div>
    <!-- 面包屑视图 -->
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">
        首页
      </el-breadcrumb-item>
      <el-breadcrumb-item>权限管理</el-breadcrumb-item>
      <el-breadcrumb-item>角色列表</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- Card -->
    <el-card>
      <el-row>
        <el-col>
          <el-button type="primary">
            添加角色
          </el-button>
        </el-col>
      </el-row>

      <!-- 角色列表区域 -->
      <el-table
        :data="rolesList"
        border
        stripe
      >
        <!-- 展开列 -->
        <el-table-column
          type="expand"
        />
        <el-table-column
          type="index"
          label="#"
        />
        <el-table-column
          prop="roleName"
          label="角色名称"
        />
        <el-table-column
          prop="roleDesc"
          label="角色描述"
        />
        <el-table-column
          label="操作"
          width="300px"
        >
          <template v-slot="scope">
            <el-button
              size="mini"
              type="primary"
              icon="el-icon-edit"
            >
              编辑
            </el-button>
            <el-button
              size="mini"
              type="danger"
              icon="el-icon-delete"
            >
              删除
            </el-button>
            <el-button
              size="mini"
              type="warning"
              icon="el-icon-setting"
            >
              分配权限
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // 所有角色列表数据
      rolesList: []
    }
  },
  created () {
    this.getRolesList()
  },
  methods: {
    async getRolesList () {
      const { data: res } = await this.$http.get('roles')
      console.log(res)
      if (res.meta.status !== 200) {
        return this.$message.error('角色列表获取失败')
      }
      this.rolesList = res.data
      return this.$message.success(res.meta.msg)
    }
  }
}
</script>

<style lang="less">

</style>
