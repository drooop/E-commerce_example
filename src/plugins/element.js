import Vue from 'vue'
import {
  Row, Col,
  Button, Form, FormItem, Input, Alert, Message, Container, Header, Aside, Main,
  Menu, MenuItem, Submenu, Breadcrumb, BreadcrumbItem, Card, Table, TableColumn,
  Switch, Tooltip, Pagination, Dialog, MessageBox
} from 'element-ui'

Vue
  .use(Button).use(Row).use(Col)
  .use(Form).use(FormItem)
  .use(Input)
  .use(Alert)
  .use(Container).use(Header).use(Aside).use(Main)
  .use(Menu).use(MenuItem).use(Submenu)
  .use(Breadcrumb).use(BreadcrumbItem)
  .use(Card).use(Input)
  .use(Table).use(TableColumn).use(Switch).use(Tooltip).use(Pagination).use(Dialog)
Vue.prototype.$message = Message
Vue.prototype.$confirm = MessageBox.confirm
