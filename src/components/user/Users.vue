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
            v-model="queryInfo.query"
            placeholder="请输入内容"
            clearable
            @clear="getUserList"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="getUserList"
            />
          </el-input>
        </el-col>
        <el-col :span="4">
          <el-button
            type="primary"
            @click="addDialogVisible = true"
          >
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
          prop="username"
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
              @change="userStateChanged(scope.row)"
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
              @click="showEditDialog(scope.row)"
            />

            <!-- 删除按钮 -->
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              @click="removeUserById(scope.row.id)"
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

      <!-- 添加用户的对话框 -->
      <el-dialog
        title="添加用户"
        :visible.sync="addDialogVisible"
        width="50%"
        @close="addFormClosed"
      >
        <!-- 内容主体区域 -->
        <el-form
          ref="addFormRef"
          :model="addForm"
          :rules="addFormRules"
          label-width="70px"
        >
          <el-form-item
            label="用户名称"
            prop="username"
          >
            <el-input v-model="addForm.username" />
          </el-form-item>
          <el-form-item
            label="用户密码"
            prop="password"
          >
            <el-input
              v-model="addForm.password"
              show-password
            />
          </el-form-item>
          <el-form-item
            label="邮箱地址"
            prop="email"
          >
            <el-input v-model="addForm.email" />
          </el-form-item>
          <el-form-item
            label="手机号码"
            prop="mobile"
          >
            <el-input v-model="addForm.mobile" />
          </el-form-item>
        </el-form>
        <!-- 底部区域 -->
        <span
          slot="footer"
          class="dialog-footer"
        >
          <el-button @click="addDialogVisible = false">取 消</el-button>
          <el-button
            type="primary"
            @click="addUser"
          >确 定</el-button>
        </span>
      </el-dialog>
      <!-- 修改用户的对话框 -->
      <el-dialog
        title="修改用户"
        :visible.sync="editDialogVisible"
        width="50%"
        @close="editDialogClosed"
      >
        <el-form
          ref="editFormRef"
          :model="editForm"
          :rules="editFormRules"
          label-width="70px"
        >
          <el-form-item
            label="用户名称"
          >
            <el-input
              v-model="editForm.username"
              disabled
            />
          </el-form-item>
          <el-form-item
            label="邮箱地址"
            prop="email"
          >
            <el-input v-model="editForm.email" />
          </el-form-item>
          <el-form-item
            label="手机号码"
            prop="mobile"
          >
            <el-input v-model="editForm.mobile" />
          </el-form-item>
        </el-form>
        <span
          slot="footer"
          class="dialog-footer"
        >
          <el-button @click="editDialogVisible = false">取 消</el-button>
          <el-button
            type="primary"
            @click="editUserInfo"
          >确 定</el-button>
        </span>
      </el-dialog>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    // 验证邮箱地址的规则
    var checkEmail = (rule, value, callback) => {
      const regEmail = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/
      if (regEmail.test(value)) {
        return callback()
      }
      callback(new Error('请输入合法的邮箱地址'))
    }

    // 验证手机号码的规则
    var checkMobile = (rule, value, callback) => {
      // 验证手机号码的正则表达式
      const regMobile = /^(0|86|17951)?(13[0-9]|15[0123456789]|17[678]|18[0-9]14[57])[0-9]{8}$/

      if (regMobile.test(value)) {
        return callback()
      }
      callback(new Error('请输入合法的手机号码'))
    }

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
      total: 0,
      // 控制 添加用户对话框 的显示与否
      addDialogVisible: false,
      // 添加用户的表单数据
      addForm: {
        username: '',
        password: '',
        email: '',
        mobile: ''
      },
      // 控制修改用户对话框的显示与否
      editDialogVisible: false,
      editForm: {},
      // 添加表单的验证规则对象
      addFormRules: {
        username: [
          { require: true, message: '请输入用户名', trigger: 'blur' },
          {
            min: 3,
            max: 10,
            message: '用户名长度在 3 到 10 个字符',
            trigger: 'blur'
          }
        ],
        password: [
          { require: true, message: '请输入密码', trigger: 'blur' },
          {
            min: 6,
            max: 15,
            message: '密码长度在 6 到 15 个字符',
            trigger: 'blur'
          }
        ],
        email: [
          { require: true, message: '请输入邮箱', trigger: 'blur' },
          { validator: checkEmail, trigger: 'blur' }

        ],
        mobile: [
          { require: true, message: '请输入手机号码', trigger: 'blur' },
          { validator: checkMobile, trigger: 'blur' }

        ]
      },
      // 修改表单的验证规则
      editFormRules: {
        email: [
          { require: true, message: '请输入邮箱地址', trigger: 'blur' },
          { validator: checkEmail, trigger: 'blur' }

        ],
        mobile: [
          { require: true, message: '请输入手机号码', trigger: 'blur' },
          { validator: checkMobile, trigger: 'blur' }

        ]
      }
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
      // console.log(res)
    },
    // 监听 pagesize 改变事件, 传递将要更新到的显示条目数
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getUserList()
    },
    // 监听 page 改变事件, 传递将要更新到的页码数
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getUserList()
    },
    async userStateChanged (userinfo) {
      // console.log(userinfo)
      const { data: res } = await this.$http.put(`users/${userinfo.id}/state/${userinfo.mg_state}`)
      if (res.meta.state !== 200) {
        userinfo.mg_state = !userinfo.mg_state
        return this.$message.error('更新用户状态失败')
      }
      this.$message('更新用户状态成功')
      // console.log(res)
    },
    addFormClosed () {
      this.$refs.addFormRef.resetFields()
    },
    addUser () {
      this.$refs.addFormRef.validate(async valid => {
        // 如果预校验失败,直接返回
        if (!valid) return
        // console.log(this.addForm)
        // 可以发起添加用户的请求
        const { data: res } = await this.$http.post('users', this.addForm)
        if (res.meta.status !== 201) {
          return this.$message.error('添加用户失败')
        }
        this.$message.success('添加用户成功')
        this.addDialogVisible = false
        this.getUserList()
      })
    },
    async showEditDialog (rowData) {
      this.editDialogVisible = true
      const { data: res } = await this.$http(`users/${rowData.id}`)
      if (res.meta.status !== 200) {
        return this.$message.error(res.meta.msg)
      }
      this.$message.success(res.meta.msg)
      this.editForm = res.data
    },
    // 监听修改用户对话框的关闭事件
    editDialogClosed () {
      this.$refs.editFormRef.resetFields()
    },
    // 修改用户信息并提交
    editUserInfo () {
      this.$refs.editFormRef.validate(async valid => {
        if (!valid) {
          return this.$message.error('该操作不合法')
        }
        const { data: res } = await this.$http.put(`users/${this.editForm.id}`,
          {
            email: this.editForm.email,
            mobile: this.editForm.mobile
          })
        if (res.meta.status !== 200) {
          return this.$message.error('用户信息更改失败')
        }
        // 关闭对话框
        this.editDialogVisible = false
        // 刷新用户列表
        this.getUserList()
        // 提示修改成功
        this.$message.success('用户信息更改成功')
      })
    },
    // 根据用户id删除对应的用户信息
    async removeUserById (id) {
      // 弹窗提示用户，询问用户是否确认删除动作
      const confirmResult = await this.$confirm('此操作将永久删除该用户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).catch(err => err)

      if (confirmResult !== 'confirm') {
        return this.$message.info('已取消删除')
      }
      const { data: res } = await this.$http.delete(`users/${id}`)
      if (res.meta.status !== 200) return this.$message.error('删除失败')
      this.$message.success(res.meta.msg)
      this.getUserList()
    }
  }
}
</script>

<style lang="less" scoped>

</style>
