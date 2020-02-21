import Vue from 'vue'
import { Button, Form, FormItem, Input, Alert, Message } from 'element-ui'

Vue.use(Button)
Vue.use(Form).use(FormItem)
Vue.use(Input)
Vue.use(Alert)
Vue.prototype.$message = Message
