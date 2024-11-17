import maya.cmds as cmds
import maya.api.OpenMaya as om
from PySide2.QtWidgets import QWidget, QPushButton, QSlider, QLabel,QCheckBox,QApplication,QComboBox,QTabWidget,QSpinBox, QTreeWidget,QTreeWidgetItem,QLineEdit
from PySide2.QtCore import Qt, QRect
from maya.OpenMayaUI import MQtUtil
from shiboken2 import wrapInstance
from functools import partial
from PySide2.QtCore import QUrl
from PySide2.QtGui import QDesktopServices
import json
import math
class RigTools(QWidget):
    def __init__(self,RT_PATH,RT_PATH_Lib):

        super(RigTools, self).__init__()
        self.RT_PATH = RT_PATH
        self.RT_PATH_Lib = RT_PATH_Lib
        # 获取屏幕分辨率
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_height = screen_geometry.height()
        # 基准分辨率
        base_height = 1080
        # 计算缩放比例
        self.hr = screen_height / base_height

        self.setGeometry(self.hr*1360,self.hr*230,self.hr*260, self.hr*240)
        self.setWindowTitle('小叶的绑定工具')
        self.setParent(wrapInstance(int(MQtUtil.mainWindow()),QWidget))
        self.setWindowFlags (Qt.Window)

        #实例变量
        self.last_spine = None
        self.last_neck = None
        self.current_index = 0
        self.cb01_isChecked = False
        self.cb02_isChecked = False

        self.initUI()

    def initUI(self):
        # 创建 QTabWidget
        self.tab_widget = QTabWidget(parent=self)
        self.tab_widget.setGeometry(0, 0, 260 * self.hr, 240 * self.hr)
        # 创建 Tab 页面
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        # 添加 Tab 页面到 QTabWidget
        self.tab_widget.addTab(tab1, "创建绑定")
        self.tab_widget.addTab(tab2, "绑定工具")
        self.tab_widget.addTab(tab3, "关于")
        # 标签
        self.ref0000 = QLabel('大臂', parent=tab1)
        self.ref0000.setGeometry(QRect(self.hr * 120, self.hr * 10, self.hr * 30, self.hr * 15))

        self.ref0001 = QLabel('小臂', parent=tab1)
        self.ref0001.setGeometry(QRect(self.hr * 185, self.hr * 10, self.hr * 30, self.hr * 15))

        self.ref0100 = QLabel('大腿', parent=tab1)
        self.ref0100.setGeometry(QRect(self.hr * 120, self.hr * 30, self.hr * 30, self.hr * 15))
        self.ref0101 = QLabel('小腿', parent=tab1)
        self.ref0101.setGeometry(QRect(self.hr * 185, self.hr * 30, self.hr * 30, self.hr * 15))

        self.ref0200 = QLabel("搜索:", parent=tab2)
        self.ref0200.setGeometry(QRect(self.hr * 120, self.hr * 10, self.hr * 30, self.hr * 15))

        self.ref0201 = QLabel("替换:", parent=tab2)
        self.ref0201.setGeometry(QRect(self.hr * 120, self.hr * 30, self.hr * 30, self.hr * 15))

        self.ref0300 = QLabel("side:", parent=tab1)
        self.ref0300.setGeometry(QRect(self.hr * 10, self.hr * 180, self.hr * 30, self.hr * 15))


        #按钮
        self.b00 = QPushButton('创建',parent=tab1)
        self.b00.setGeometry(QRect(self.hr*65, self.hr*10, self.hr*45, self.hr*30))
        self.b00.clicked.connect(self.import_biped)
        
        self.b01 = QPushButton('创建/更新控制器',parent=tab1)
        self.b01.setGeometry(QRect(self.hr*10, self.hr*50, self.hr*100, self.hr*30))
        self.b01.clicked.connect(self.import_controls)

        self.b02 = QPushButton('添加Twist', parent=tab1)
        self.b02.setGeometry(QRect(self.hr * 130, self.hr * 50, self.hr * 100, self.hr * 30))
        self.b02.clicked.connect(self.create_twist)

        self.b03 = QPushButton('添加拉伸', parent=tab1)
        self.b03.setGeometry(QRect(self.hr * 10, self.hr * 130, self.hr * 100, self.hr * 30))
        self.b03.clicked.connect(self.create_stretch)

        self.b03 = QPushButton('镜像曲线', parent=tab2)
        self.b03.setGeometry(QRect(self.hr*10, self.hr*10, self.hr*100, self.hr*30))
        self.b03.clicked.connect(self.mirror_curve)
        
        self.b04 = QPushButton('替换形状', parent=tab2)
        self.b04.setGeometry(QRect(self.hr*10, self.hr*50, self.hr*100, self.hr*30))
        self.b04.clicked.connect(self.replace_shape)
        
        self.b0500 = QPushButton('添加', parent=tab2)
        self.b0500.setGeometry(QRect(self.hr*10, self.hr*90, self.hr*45, self.hr*30))
        self.b0500.clicked.connect(self.add_shape)
        self.b0501 = QPushButton('移除', parent=tab2)
        self.b0501.setGeometry(QRect(self.hr*65, self.hr*90, self.hr*45, self.hr*30))
        self.b0501.clicked.connect(self.remove_shape)
        
        self.b06 = QPushButton('完成绑定！',parent=tab1)
        self.b06.setGeometry(QRect(self.hr*10, self.hr*90, self.hr*100, self.hr*30))
        self.b06.clicked.connect(self.rig)
        
        self.b07 = QPushButton('FK链', parent=tab1)
        self.b07.setGeometry(QRect(self.hr*130, self.hr*170, self.hr*50, self.hr*30))
        self.b07.clicked.connect(self.create_ctrl)
        
        self.b08 = QPushButton('查找重名', parent=tab2)
        self.b08.setGeometry(QRect(self.hr*10, self.hr*130, self.hr*100, self.hr*30))
        self.b08.clicked.connect(self.find_duplicate_names)

        self.b09 = QPushButton('添加Average', parent=tab1)
        self.b09.setGeometry(QRect(self.hr * 130, self.hr * 90, self.hr * 100, self.hr * 30))
        self.b09.clicked.connect(self.create_average)

        self.b09 = QPushButton('添加Push', parent=tab1)
        self.b09.setGeometry(QRect(self.hr * 130, self.hr * 130, self.hr * 100, self.hr * 30))
        self.b09.clicked.connect(self.create_push)

        self.b10 = QPushButton("搜索替换", parent=tab2)
        self.b10.setGeometry(QRect(self.hr * 130, self.hr * 50, self.hr * 100, self.hr * 30))
        self.b10.clicked.connect(self.search_replace)

        self.b11 = QPushButton("吸附", parent=tab2)
        self.b11.setGeometry(QRect(self.hr * 130, self.hr * 90, self.hr * 100, self.hr * 30))
        self.b11.clicked.connect(self.snap_to_pivot)

        self.b12 = QPushButton("创建刀光", parent=tab2)
        self.b12.setGeometry(QRect(self.hr * 130, self.hr * 130, self.hr * 100, self.hr * 30))
        self.b12.clicked.connect(self.create_ghost)

        self.b12 = QPushButton("万向驱动", parent=tab2)
        self.b12.setGeometry(QRect(self.hr * 130, self.hr * 170, self.hr * 100, self.hr * 30))
        self.b12.clicked.connect(self.universal_drive)

        #self.b13 = QPushButton("清除关节旋转", parent=tab2)
        #self.b13.setGeometry(QRect(self.hr * 10, self.hr * 170, self.hr * 100, self.hr * 30))
        #self.b13.clicked.connect(self.rotate_to_jointOrient)

        self.b21 = QPushButton('作者主页', parent=tab3)
        self.b21.setGeometry(QRect(self.hr * 10, self.hr * 10, self.hr * 100, self.hr * 30))
        self.b21.clicked.connect(lambda: QDesktopServices.openUrl(QUrl('https://space.bilibili.com/341240492')))

        self.b22 = QPushButton('打开脚本目录', parent=tab3)
        self.b22.setGeometry(QRect(self.hr * 10, self.hr * 50, self.hr * 100, self.hr * 30))
        self.b22.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(f'file:///{self.RT_PATH}')))
        #数字输入
        self.spinBox_00 = QSpinBox(parent=tab1)
        self.spinBox_00.setGeometry(QRect(self.hr * 145, self.hr * 7, self.hr * 40, self.hr * 20))
        self.spinBox_00.setRange(0, 10)  # 设置范围
        self.spinBox_00.setValue(2)  # 设置初始值

        self.spinBox_01 = QSpinBox(parent=tab1)
        self.spinBox_01.setGeometry(QRect(self.hr * 210, self.hr * 7, self.hr * 40, self.hr * 20))
        self.spinBox_01.setRange(0, 10)  # 设置范围
        self.spinBox_01.setValue(2)  # 设置初始值

        self.spinBox_02 = QSpinBox(parent=tab1)
        self.spinBox_02.setGeometry(QRect(self.hr * 145, self.hr * 27, self.hr * 40, self.hr * 20))
        self.spinBox_02.setRange(0, 10)  # 设置范围
        self.spinBox_02.setValue(2)  # 设置初始值

        self.spinBox_03 = QSpinBox(parent=tab1)
        self.spinBox_03.setGeometry(QRect(self.hr * 210, self.hr * 27, self.hr * 40, self.hr * 20))
        self.spinBox_03.setRange(0, 10)  # 设置范围
        self.spinBox_03.setValue(2)  # 设置初始值
        #输入框
        self.le0000 = QLineEdit(parent=tab2)
        self.le0000.setGeometry(QRect(self.hr * 150, self.hr * 10, self.hr * 80, self.hr * 20))

        self.le0001 = QLineEdit(parent=tab2)
        self.le0001.setGeometry(QRect(self.hr * 150, self.hr * 30, self.hr * 80, self.hr * 20))

        self.le0100 = QLineEdit(parent=tab1)
        self.le0100.setGeometry(QRect(self.hr * 40, self.hr * 175, self.hr * 70, self.hr * 25))
        self.le0100.setText('l,r')
        self.side_list = ['l','r']
        self.le0100.textChanged.connect(self.side_changed)

        #选框
        self.cb01 = QCheckBox('缩放',parent=tab1)
        self.cb01.setGeometry(QRect(self.hr*190, self.hr*160, self.hr*50, self.hr*30))
        self.cb01.stateChanged.connect(self.update_cb01)

        self.cb02 = QCheckBox('旋转跟随', parent=tab1)
        self.cb02.setGeometry(QRect(self.hr * 190, self.hr * 180, self.hr * 80, self.hr * 30))
        self.cb02.stateChanged.connect(self.update_cb02)

        #枚举
        self.cb00 = QComboBox(parent=tab1)
        self.cb00.setGeometry(QRect(self.hr*10, self.hr*10, self.hr*50, self.hr*30))
        self.cb00.addItem("双足")
        self.cb00.addItem("UE双足")
        self.cb00.addItem("爪类")
        self.cb00.addItem("蹄类")
        self.cb00.addItem("鸟类")
        self.cb00.currentIndexChanged.connect(self.on_combo_change)
    def on_combo_change(self, index):
        #枚举值变化函数
        self.current_index = index
        try:
            self.b00.clicked.disconnect()
        except TypeError:
            # 如果没有连接，断开操作会抛出 TypeError
            pass
        if index == 0:
            self.b00.clicked.connect(self.import_biped)
        elif index == 1:
            self.b00.clicked.connect(self.import_bipedUE)
        elif index == 2:
            self.b00.clicked.connect(partial(self.import_file,'joints_tetrapod'))

    def side_changed(self):
        self.side_list = self.le0100.text().split(',')

    def update_cb01(self):
        if self.cb01.isChecked():
            self.cb01_isChecked = True
        else:
            self.cb01_isChecked = False
    def update_cb02(self):
        if self.cb02.isChecked():
            self.cb02_isChecked = True
        else:
            self.cb02_isChecked = False

    '''
    导入双足骨骼
    '''
    def import_biped(self):
        if cmds.objExists('root') and not cmds.objExists('heelPivot_l'):
            self.import_file('joints_foot')
        elif not cmds.objExists('root') and cmds.objExists('heelPivot_l'):
            self.import_file('joints_biped')
        elif not cmds.objExists('root') and not cmds.objExists('heelPivot_l'):
            self.import_file('joints_biped')
            self.import_file('joints_foot')
        else:
            cmds.warning('已导入骨骼')
    '''
    导入UE双足
    '''
    def import_bipedUE(self):
        if cmds.objExists('root') and not cmds.objExists('heelPivot_l'):
            self.import_file('joints_foot')
        elif not cmds.objExists('root') and cmds.objExists('heelPivot_l'):
            self.import_file('joints_bipedUE')
        elif not cmds.objExists('root') and not cmds.objExists('heelPivot_l'):
            self.import_file('joints_bipedUE')
            self.import_file('joints_foot')
        else:
            cmds.warning('已导入骨骼')

    '''
    导入文件
    '''
    def import_file(self,file_name):
        path = self.RT_PATH_Lib + '/'+file_name+'.ma'
        try:
            cmds.file(path, i=True, type="mayaAscii", ignoreVersion=True, ra=True, mergeNamespacesOnClash=False, namespace=":", options="v=0;", pr=True)
        except:
            cmds.warning('未能导入'+path)

    '''
    保存文件
    '''
    def save_file(self,file_postfix):
        current_file = cmds.file(query=True, sceneName=True)
        if current_file:
            # 确保当前场景已保存
            cmds.file(save=True)
            file_directory, file_name = os.path.split(current_file)
            file_base_name, file_extension = os.path.splitext(file_name)

            # 创建新的文件名，并拼接成完整路径（假设保存到当前文件夹）
            new_file_name = f"{file_base_name}_{file_postfix}{file_extension}"
            new_file_path = os.path.join(file_directory, new_file_name)

            # 使用 shutil.copy() 复制当前文件
            shutil.copy(current_file, new_file_path)
            cmds.warning(f"文件已保存副本为: {new_file_path}")
        else:
            cmds.warning("当前场景未保存，无法创建副本。")

    '''
    安全父级
    '''
    def safe_parent(self,childs, parent):
        if isinstance(childs, str):
            childs = [childs]
        for child in childs:
            # 检查目标对象是否已经是父对象的子对象
            if cmds.objExists(child) and cmds.objExists(parent):
                current_parent = cmds.listRelatives(child, parent=True)
                if current_parent is None or current_parent[0] != parent:
                    cmds.parent(child, parent)
    
    '''
    安全删除
    '''
    def safe_delete(self,objs):
        if isinstance(objs, str):
            objs = [objs]
        for obj in objs:
            if cmds.objExists(obj):
                cmds.delete(obj)
    '''
    安全创建节点
    '''
    def safe_createNode(self,node,name):
        if not cmds.objExists(name):
            cmds.createNode(node,name=name)
    '''
    创建condition
    '''
    def create_condition(self,name=''):
        if name=='':
            name='con_00'
        self.safe_createNode('condition',name=name)
        self.setAttrAdv(name,['colorIfTrueR','colorIfTrueG','colorIfTrueB'],value=1)
        self.setAttrAdv(name, ['colorIfFalseR', 'colorIfFalseG', 'colorIfFalseB'], value=0)
    '''
    冻结变换
    '''
    def freeze_transform(self,name=[],t=0,r=1,s=1):
        cmds.select(name)
        cmds.makeIdentity(apply=True, t=t, r=r, s=0, n=0, pn=1)
        cmds.select(clear=True)
    '''
    创建骨骼
    '''
    def create_joint(self,name='',translate=[0,0,0], rotate=[0,0,0], parent=None,update=True):
        if name=='':
            name='jnt_01'
        if not cmds.objExists(name):
            cmds.createNode('joint', name=name)
            self.safe_parent(name, parent)
            cmds.setAttr(name + '.tx', translate[0])
            cmds.setAttr(name + '.ty', translate[1])
            cmds.setAttr(name + '.tz', translate[2])
            cmds.setAttr(name + '.jointOrientX', rotate[0])
            cmds.setAttr(name + '.jointOrientY', rotate[1])
            cmds.setAttr(name + '.jointOrientZ', rotate[2])
        else:
            if update:
                self.safe_parent(name, parent)
                cmds.setAttr(name + '.tx', translate[0])
                cmds.setAttr(name + '.ty', translate[1])
                cmds.setAttr(name + '.tz', translate[2])
                cmds.setAttr(name + '.jointOrientX', rotate[0])
                cmds.setAttr(name + '.jointOrientY', rotate[1])
                cmds.setAttr(name + '.jointOrientZ', rotate[2])
        return name
    '''
    分配twist骨骼位置
    '''
    def between_joints(self,a, b,name,parent, number):
        # 获取骨骼 a 和骨骼 b 的世界空间位置
        pos_a = cmds.xform(a, q=True, ws=True, t=True)
        pos_b = cmds.xform(b, q=True, ws=True, t=True)
        # 计算从 a 到 b 的方向向量
        vector_ab = [pos_b[i] - pos_a[i] for i in range(3)]
        # 计算每个新骨骼的位置增量
        increment = [vector_ab[i] / (number + 1) for i in range(3)]
        for i in range(1, number + 1):
            # 计算每个新骨骼的位置
            new_pos = [pos_a[j] + increment[j] * i for j in range(3)]
            side=a.split('_')[1]
            if not cmds.objExists(f'{name}_twist_{str(i).zfill(2)}_{side}'):
                joint=self.create_joint(name=f'{name}_twist_{str(i).zfill(2)}_{side}', parent=parent)
                cmds.xform(joint,ws=True,t=new_pos)
    '''
    计算距离
    '''

    def calculate_distance(self,obj1, obj2):
        # 获取物体的位置
        pos1 = cmds.xform(obj1, query=True, translation=True, worldSpace=True)
        pos2 = cmds.xform(obj2, query=True, translation=True, worldSpace=True)

        # 计算距离
        distance = ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2) ** 0.5
        return distance
    '''
    镜像曲线
    '''
    def mirror_curve(self):
        selections = cmds.ls(selection=True)
        if len(selections)==2:
            curve1 = selections[0]
            curve2 = selections[1]
            # 获取曲线1的所有形状节点
            curve1_shapes = cmds.listRelatives(curve1, shapes=True, fullPath=True)
            curve2_shapes = cmds.listRelatives(curve2, shapes=True, fullPath=True)
            
            if len(curve1_shapes) != len(curve2_shapes):
                cmds.error('曲线的形状数量不匹配')
                return
            
            for shape1, shape2 in zip(curve1_shapes, curve2_shapes):
                # 获取曲线形状的控制点数量
                num_cvs = cmds.getAttr(shape1 + ".spans") + cmds.getAttr(shape1 + ".degree")
                
                for i in range(num_cvs):
                    # 获取曲线形状1当前控制点的世界位置
                    pos = cmds.pointPosition(shape1 + ".cv[{}]".format(i), world=True)
                    
                    # 计算镜像位置
                    mirrored_pos = (-pos[0], pos[1], pos[2])
                    
                    # 设置曲线形状2当前控制点的位置
                    cmds.move(mirrored_pos[0], mirrored_pos[1], mirrored_pos[2], shape2 + ".cv[{}]".format(i), absolute=True, worldSpace=True)
        else:
            cmds.warning('选择的曲线数量不等于2')
    '''
    替换形状
    '''
    def replace_shape(self):
        selected_objects = cmds.ls(selection=True)
        #复制一份
        new=cmds.duplicate(selected_objects[0])
        #获取形状
        shapeA=cmds.listRelatives(selected_objects[0],children=True,shapes=True)
        shapeB=cmds.listRelatives(selected_objects[1],children=True,shapes=True)
        #将形状添加到物体
        cmds.parent(shapeA,selected_objects[1],shape=True,addObject=True)
        cmds.delete(shapeB)
        cmds.rename(shapeA,shapeB)
        cmds.delete(selected_objects[0])
        cmds.select(new)
    '''
    添加形状
    '''
    def add_shape(self):
        selected_objects = cmds.ls(selection=True)
        #复制一份
        new=cmds.duplicate(selected_objects[0])
        #获取形状
        shapeA=cmds.listRelatives(selected_objects[0],children=True,shapes=True)
        shapeB=cmds.listRelatives(selected_objects[1],children=True,shapes=True)
        cmds.parent(shapeA,selected_objects[1],shape=True,addObject=True)
        cmds.delete(selected_objects[0])
        cmds.select(new)
        
    '''
    移除形状
    '''
    def remove_shape(self):
        cmds.parent(cmds.ls(selection=True),shape=True,removeObject=True)
    '''
    查找重名
    '''
    def find_duplicate_names(self):
        # 获取场景中所有对象的名称
        all_objects = cmds.ls()
    
        # 创建一个空字典来存储对象名称及其计数
        object_counts = {}
    
        # 遍历所有对象，计算每个名称出现的次数
        for obj in all_objects:
            # 使用split函数获取对象的短名称
            short_name = obj.split('|')[-1]
    
            if short_name in object_counts:
                object_counts[short_name] += 1
            else:
                object_counts[short_name] = 1
        duplicate_names = []
        # 打印出现重复的对象名称及其计数
        for obj, count in object_counts.items():
            if count > 1:
                duplicate_names.append(obj)
        
        if duplicate_names:
            cmds.warning('重复名称：'+ ', '.join(duplicate_names))
        else:
            cmds.warning('没有重复名称')
    '''
    关节方向最大值
    '''

    def max_joint_orient(self,joint_name):
        # 获取关节的旋转轴向
        joint_orient = cmds.getAttr(f'{joint_name}.jointOrient')[0]

        # 绝对值比较 X, Y, Z 三个方向
        axis_values = {
            'y': abs(joint_orient[1]),
            'z': abs(joint_orient[2])
        }

        # 获取绝对值最大的轴向
        max_axis = max(axis_values, key=axis_values.get)

        # 如果最大值为 Z，输出 Y；如果最大值为 Y，输出 Z
        if max_axis == 'z':
            up_axis = 'y'
        elif max_axis == 'y':
            up_axis = 'z'

        return max_axis, up_axis
    '''
    创建/更新躯干
    '''
    def import_controls(self):
        if not cmds.objExists('ctrl_c_root'):
            self.import_file('controls_root')
        #判断是否导入了文件
        if not cmds.objExists('ctrl_c_cog'):
            if self.current_index ==0:
                self.import_file('controls_body')
            elif self.current_index ==1:
                self.import_file('controls_bodyUE')
        self.safe_parent('grp_c_body','ctrl_c_root')
        #对齐躯干
        cmds.matchTransform('zero_c_cog','spine_01',position=True)
        cmds.matchTransform('zero_c_spineA','spine_01')
        cmds.matchTransform('grp_c_spineIk','spine_01')
        cmds.select('crv_c_spine')
        cmds.DeleteHistory()
        cmds.setAttr('crv_c_spine.inheritsTransform',False)
        spine_count = 10  # 假设最多有10个spine对象
        #获取crv_c_spine的顶点数量
        crv_c_spine_pivot = cmds.getAttr("crv_c_spine.spans") + cmds.getAttr("crv_c_spine.degree")
        skinSpine_ctrl = []
        #控制器对齐到骨骼，如果没有该骨骼删除对应的控制器
        for i in range(1, spine_count + 1):  # 从spine_01开始遍历
            spine_name = f'spine_{str(i).zfill(2)}'#蒙皮骨骼名称
            
            
            zero_name = f'zero_c_spine{chr(65 + (i - 1))}'#躯干FK zero名称
            ctrl_name = f'ctrl_c_spine{chr(65 + (i - 1))}'#躯干FK控制器名称
            next_zero_name = f'zero_c_spine{chr(65 + (i))}'#下一个躯干FK zero名称
            
            zero_spineIk = f'zero_c_spineIk{chr(65 + (i - 1))}'#躯干IK zero名称
            ctrl_spineIk = f'ctrl_c_spineIk{chr(65 + (i - 1))}'#躯干IK 控制器名称
            
            joint_c_spineIk = f'jnt_c_spine{chr(65 + (i - 1))}'#躯干IK joint名称
            before_joint_c_spineIk = f'jnt_c_spine{chr(65 + (i - 2))}'#上一级躯干IK joint名称
            next_joint_c_spineIk_list = f'jnt_c_spine{chr(65 + (i))}'#下一级躯干IK joint名称
            
            #如果没有下一级则 next_joint_c_spineIk = None
            if next_joint_c_spineIk_list:
                next_joint_c_spineIk = next_joint_c_spineIk_list[0]
            else:
                next_joint_c_spineIk = None
            
            if cmds.objExists(spine_name):
                cmds.matchTransform(zero_name, spine_name)
                cmds.matchTransform(zero_spineIk, spine_name)
                cmds.matchTransform(joint_c_spineIk, spine_name)
                self.freeze_transform([joint_c_spineIk])
                spine_joint_position = cmds.xform(spine_name, query=True, worldSpace=True, translation=True)
                
                cmds.move(spine_joint_position[0], spine_joint_position[1], spine_joint_position[2], f'crv_c_spine.cv[{i-1}]', absolute=True)
                last_i = i
                
                last_spine_name = spine_name
                last_ctrl_name = ctrl_name
                last_joint_c_spineIk = joint_c_spineIk
                
                skinSpine_ctrl.append(ctrl_spineIk)
            else:
                if cmds.objExists(next_zero_name):
                    cmds.parent(next_zero_name,last_ctrl_name)
                if next_joint_c_spineIk and cmds.objExists(next_joint_c_spineIk):
                    cmds.parent(next_joint_c_spineIk,before_joint_c_spineIk)
                
                self.safe_delete([zero_name,zero_spineIk,joint_c_spineIk])

        #如果spine骨骼不足以生成ik则删除spineIK
        if last_spine_name == 'spine_02':
            self.safe_delete(['grp_c_spineIk','crv_c_spine'])

        else:
            if not cmds.objExists('jnt_c_neck'):
                self.create_joint(name='jnt_c_neck',parent=last_joint_c_spineIk)
            cmds.matchTransform('jnt_c_neck','neck_01')
            self.freeze_transform(['jnt_c_neck'])

            cmds.matchTransform('zero_c_spineIk','neck_01',position=True)
            cmds.xform('zero_c_spineIk',rotation=['0','0','0'],worldSpace=True)

            cmds.matchTransform('jnt_c_neckIk','neck_01')

            cmds.matchTransform('crv_c_spineFk',last_spine_name)
            cmds.matchTransform('crv_c_spineFk','ctrl_c_spineIk',rotation=True)
            #对齐最后一个spine曲线顶点并删除多余的顶点
            neck_joint_position = cmds.xform('neck_01', query=True, worldSpace=True, translation=True)
            cmds.move(neck_joint_position[0], neck_joint_position[1], neck_joint_position[2], f'crv_c_spine.cv[{last_i}]', absolute=True)
            if crv_c_spine_pivot > last_i+1:
                cmds.delete(f'crv_c_spine.cv[{last_i+1}:{crv_c_spine_pivot - 1}]')
            #绑定蒙皮spine曲线
            skinSpine_joint = ['jnt_c_spineIkA','jnt_c_neckIk']+skinSpine_ctrl[1:]
            cmds.skinCluster(skinSpine_joint, 'crv_c_spine', toSelectedBones=True, normalizeWeights=1,name='sc_c_spine')


        #对齐脖子和头部
        cmds.matchTransform('grp_c_spineC',last_spine_name)
        if cmds.objExists('crv_c_neck'):
            crv_c_neck_pivot = cmds.getAttr("crv_c_neck.spans") + cmds.getAttr("crv_c_neck.degree")
        if cmds.objExists('neck_03'):#如果可以生成脖子IK
            self.safe_delete('zero_c_neck')
            skinNeck_ctrl=[]
            neck_count = 10
            #循环对齐脖子
            for n in range(1, neck_count + 1):
                neck_name = f'neck_{str(n).zfill(2)}'
                next_neck_name=f'neck_{str(n+1).zfill(2)}'
                zero_neck_name = f'zero_c_neck{chr(65 + (n - 1))}'#脖子FK名称
                ctrl_neck_name = f'ctrl_c_neck{chr(65 + (n - 1))}'
                next_zero_neck_name = f'zero_c_neck{chr(65 + (n))}'
                
                joint_c_neck = f'jnt_c_neck{chr(65 + (n - 1))}'#脖子IK骨骼名称
                before_joint_c_neck = f'jnt_c_neck{chr(65 + (n - 2))}'
                next_joint_c_neck = f'jnt_c_neck{chr(65 + (n))}'
                
                zero_c_neckIk = f'zero_c_neckIk{chr(65 + (n - 1))}'#脖子IK控制器名称
                ctrl_c_neckIk = f'ctrl_c_neckIk{chr(65 + (n - 1))}'
                
                if cmds.objExists(neck_name):
                    cmds.matchTransform(zero_neck_name,neck_name)
                    cmds.matchTransform(joint_c_neck,neck_name)
                    cmds.matchTransform(zero_c_neckIk,neck_name)
                    neck_joint_position = cmds.xform(neck_name, query=True, worldSpace=True, translation=True)
                    cmds.move(neck_joint_position[0], neck_joint_position[1], neck_joint_position[2],f'crv_c_neck.cv[{n - 1}]', absolute=True)
                    last_ctrl_neck_name = ctrl_neck_name
                    last_joint_c_neck = joint_c_neck
                    skinNeck_ctrl.append(ctrl_c_neckIk)

                    last_n = n
                    
                else:
                    if cmds.objExists(next_zero_neck_name):
                        self.safe_parent(next_zero_neck_name,last_ctrl_neck_name)
                        self.safe_parent(next_joint_c_neck,last_joint_c_neck)
                    
                    self.safe_delete([zero_neck_name,joint_c_neck,zero_c_neckIk])

            self.safe_parent('zero_c_head',last_ctrl_neck_name)
            cmds.matchTransform('zero_c_head','head')
            cmds.matchTransform('zero_c_headIk','head',position=True)
            if not cmds.objExists('jnt_c_head'):
                cmds.joint(name='jnt_c_head')
                cmds.parent('jnt_c_head',last_joint_c_neck)
            cmds.matchTransform('jnt_c_head','head')
            
            #对齐最后一个neck曲线顶点并删除多余的顶点
            cmds.matchTransform('jnt_c_headIk','head')
            head_joint_position = cmds.xform('head', query=True, worldSpace=True, translation=True)
            cmds.move(head_joint_position[0], head_joint_position[1], head_joint_position[2], f'crv_c_neck.cv[{last_n}]', absolute=True)
            if crv_c_neck_pivot > last_n+1:
                cmds.delete(f'crv_c_neck.cv[{last_n+1}:{crv_c_neck_pivot}]')
            #绑定蒙皮neck曲线
            cmds.select('crv_c_neck')
            cmds.DeleteHistory()
            skinNeck_joint = ['jnt_c_neckIkA','jnt_c_headIk']+skinNeck_ctrl[1:]
            cmds.skinCluster(skinNeck_joint, 'crv_c_neck', toSelectedBones=True, normalizeWeights=1,name='sc_c_neck')
            
        else:#如果无法生成脖子IK
            self.safe_delete(['grp_c_neckIk','crv_c_neck','zero_c_neckA'])

            self.safe_parent('zero_c_head','ctrl_c_neck')
            cmds.matchTransform('zero_c_neck','neck_01')
            cmds.matchTransform('zero_c_head','head')

        #对齐尾巴
        if  not cmds.objExists('tail_01'):#判断有无尾巴
            self.safe_delete(['zero_c_tail_01', 'crv_c_tail'])
        else:
            cmds.select('crv_c_tail')
            cmds.DeleteHistory()
            cmds.matchTransform('zero_c_tail_01','tail_01')
            tail_count = 10
            crv_c_tail_pivot = cmds.getAttr("crv_c_tail.spans") + cmds.getAttr("crv_c_tail.degree")
            skinTail_ctrl = []
            tik = 1
            for t in range(2, tail_count + 1):
                tail_name = f'tail_{str(t).zfill(2)}'

                zero_tail_name = f'zero_c_tail_{str(t).zfill(2)}'  # 尾巴FK名称
                ctrl_tail_name = f'ctrl_c_tail_{str(t).zfill(2)}'
                next_zero_tail_name = f'zero_c_tail_{str(t+1).zfill(2)}'

                joint_c_tail = f'jnt_c_tail_{str(t).zfill(2)}'  # 尾巴IK骨骼名称
                before_joint_c_tail = f'jnt_c_neck_{str(t-1).zfill(2)}'
                next_joint_c_tail = f'jnt_c_tail_{str(t+1).zfill(2)}'

                if cmds.objExists(tail_name):
                    last_tail_name = tail_name
                    if t ==2:
                        cmds.matchTransform('grp_c_tailIk',tail_name)
                    cmds.matchTransform(zero_tail_name,tail_name)
                    cmds.matchTransform(joint_c_tail,tail_name)
                    tail_joint_position = cmds.xform(tail_name, query=True, worldSpace=True, translation=True)

                    cmds.move(tail_joint_position[0], tail_joint_position[1], tail_joint_position[2],
                              f'crv_c_tail.cv[{t - 2}]', absolute=True)
                    last_ctrl_tail_name = ctrl_tail_name
                    last_joint_c_tail = joint_c_tail
                    last_t = t
                    if t%2==0:# 只有在 t 为偶数时执行
                        zero_c_tailIk = f'zero_c_tailIk_{str(tik).zfill(2)}'  # 尾巴IK控制器名称
                        ctrl_c_tailIk = f'ctrl_c_tailIk_{str(tik).zfill(2)}'

                        cmds.matchTransform(zero_c_tailIk,tail_name,position=True)
                        cmds.xform(zero_c_tailIk,rotation=[0,0,0],worldSpace=True)
                        cmds.setAttr(f'{ctrl_c_tailIk}.rx', lock=False)
                        cmds.setAttr(f'{ctrl_c_tailIk}.ry', lock=False)
                        cmds.setAttr(f'{ctrl_c_tailIk}.rz', lock=False)
                        cmds.matchTransform(ctrl_c_tailIk,tail_name)
                        self.freeze_transform(ctrl_c_tailIk)
                        cmds.setAttr(f'{ctrl_c_tailIk}.rx', lock=True)
                        cmds.setAttr(f'{ctrl_c_tailIk}.ry', lock=True)
                        cmds.setAttr(f'{ctrl_c_tailIk}.rz', lock=True)
                        last_tik = tik
                        skinTail_ctrl.append(ctrl_c_tailIk)
                        tik+=1
                else:
                    self.safe_parent(next_zero_tail_name,last_ctrl_tail_name)
                    self.safe_parent(next_joint_c_tail,last_joint_c_tail)
                    self.safe_delete([zero_tail_name,joint_c_tail])
            if last_t<=3:#如果不能生成尾巴Ik
                self.safe_delete(['grp_c_tailIk','crv_c_tail'])
            else:
                #创建最后一节ik骨骼
                end_joint_c_tail = f'jnt_c_tail_{str(last_t+1).zfill(2)}'
                if not cmds.objExists(end_joint_c_tail):
                    cmds.joint(name=end_joint_c_tail)
                self.safe_parent(end_joint_c_tail,last_joint_c_tail)
                lm = cmds.xform(last_joint_c_tail,query=True,matrix=True)
                cmds.xform(end_joint_c_tail,matrix = lm)
                self.freeze_transform(end_joint_c_tail)
                #最后一个ik控制器对齐到最后一节ik骨骼
                cmds.matchTransform(f'zero_c_tailIk_{str(last_tik+1).zfill(2)}', end_joint_c_tail)
                cmds.xform(f'zero_c_tailIk_{str(last_tik+1).zfill(2)}', rotation=[0, 0, 0], worldSpace=True)
                for ti in range(last_tik+2,7):
                    zero_c_tailIk = f'zero_c_tailIk_{str(ti).zfill(2)}'
                    self.safe_delete(zero_c_tailIk)

                etw = cmds.xform(end_joint_c_tail, query=True, translation=True,worldSpace=True)
                cmds.move(etw[0], etw[1], etw[2],f'crv_c_tail.cv[{last_t-1}]', absolute=True)

                if crv_c_tail_pivot > last_t:
                    cmds.delete(f'crv_c_tail.cv[{last_t}:{crv_c_tail_pivot}]')
                # 绑定蒙皮tail曲线

                skinTail_joint = [ f'ctrl_c_tailIk_{str(last_tik+1).zfill(2)}'] + skinTail_ctrl
                cmds.skinCluster(skinTail_joint, 'crv_c_tail', toSelectedBones=True, normalizeWeights=1,name='sc_c_tail')
        #导入胳膊
        side = self.side_list
        for l in side:
            if cmds.objExists(f'clavicle_{l}'):
                cmds.matchTransform(f'zero_{l}_shoulder', f'clavicle_{l}')
                if not cmds.objExists('clavicle_r'):
                    cmds.mirrorJoint('clavicle_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=("_l", "_r"))
            if not cmds.objExists(f'upperarm_{l}'):
                cmds.warning(f'没有找到upperarm_{l}')
            else:
                # 判断是否导入了文件
                if not cmds.objExists(f'grp_{l}_arm'):
                    self.import_file(f'controls_{l}_arm')

                self.safe_parent(f'grp_{l}_arm', 'ctrl_c_root')
                # 左臂ik
                cmds.matchTransform(f'jnt_{l}_upperarmIk', f'upperarm_{l}')
                cmds.matchTransform(f'jnt_{l}_forearmIk', f'lowerarm_{l}')
                cmds.matchTransform(f'jnt_{l}_handIk', f'hand_{l}')
                self.freeze_transform(name=[f'jnt_{l}_upperarmIk', f'jnt_{l}_forearmIk', f'jnt_{l}_handIk'])

                cmds.matchTransform(f'zero_{l}_handIk', f'hand_{l}', position=True)
                cmds.matchTransform(f'ctrl_{l}_handIk', f'hand_{l}', rotation=True)
                self.freeze_transform([f'ctrl_{l}_handIk'])
                self.safe_parent(f'zero_{l}_armPv', f'jnt_{l}_forearmIk')
                cmds.xform(f'zero_{l}_armPv', translation=[0, 0, 0])
                rate = cmds.getAttr(f'lowerarm_{l}.tx') / 27
                max_axis,up_axis = self.max_joint_orient(f'jnt_{l}_forearmIk')
                up_rate=rate
                if up_axis=='y':
                    up_rate=rate*-1
                cmds.setAttr(f'zero_{l}_armPv.tx', -13 * rate)
                cmds.setAttr(f'zero_{l}_armPv.t{up_axis}', -27 * up_rate)
                self.safe_parent(f'zero_{l}_armPv', f'grp_{l}_armIk')

                # 左臂fk
                cmds.matchTransform(f'zero_{l}_upperarmFk', f'upperarm_{l}')
                cmds.matchTransform(f'zero_{l}_forearmFk', f'lowerarm_{l}')
                cmds.matchTransform(f'zero_{l}_handFk', f'hand_{l}')

                cmds.setAttr(f"crv_{l}_armFkPv.translateX", lock=False)
                cmds.setAttr(f"crv_{l}_armFkPv.translateY", lock=False)
                cmds.setAttr(f"crv_{l}_armFkPv.translateZ", lock=False)
                cmds.setAttr(f"crv_{l}_armFkPv.rotateX", lock=False)
                cmds.setAttr(f"crv_{l}_armFkPv.rotateY", lock=False)
                cmds.setAttr(f"crv_{l}_armFkPv.rotateZ", lock=False)
                cmds.matchTransform(f'crv_{l}_armFkPv', f'ctrl_{l}_armPv')

                cmds.matchTransform(f'zero_{l}_armIkFkText', f'lowerarm_{l}')
                self.safe_parent(f'zero_{l}_armIkFkText', f'lowerarm_{l}')
                cmds.setAttr(f'zero_{l}_armIkFkText.tx', 13 * rate)
                cmds.setAttr(f'zero_{l}_armIkFkText.t{max_axis}', 3.8 * rate)
                cmds.setAttr(f'zero_{l}_armIkFkText.r{up_axis}', 90)
                if max_axis=='z':
                    cmds.setAttr(f'zero_{l}_armIkFkText.r{up_axis}', -90)
                    cmds.setAttr(f'zero_{l}_armIkFkText.rx', 90)
                self.safe_parent(f'zero_{l}_armIkFkText', f'grp_{l}_arm')

                # 左臂手指
                cmds.matchTransform(f'grp_{l}_finger', f'hand_{l}')
                cmds.matchTransform(f'zero_{l}_finPinkyCarpal', f'hand_{l}')
                self.match_finger(finger_joints=[f'thumb_01_{l}', f'thumb_02_{l}', f'thumb_03_{l}'],
                                  zero_joints=[f'zero_{l}_finThumbA', f'zero_{l}_finThumbB', f'zero_{l}_finThumbC'])
                self.match_finger(finger_joints=[f'index_01_{l}', f'index_02_{l}', f'index_03_{l}'],
                                  zero_joints=[f'zero_{l}_finIndexA', f'zero_{l}_finIndexB', f'zero_{l}_finIndexC'])
                self.match_finger(finger_joints=[f'middle_01_{l}', f'middle_02_{l}', f'middle_03_{l}'],
                                  zero_joints=[f'zero_{l}_finMidA', f'zero_{l}_finMidB', f'zero_{l}_finMidC'])
                self.match_finger(finger_joints=[f'ring_01_{l}', f'ring_02_{l}', f'ring_03_{l}'],
                                  zero_joints=[f'zero_{l}_finRingA', f'zero_{l}_finRingB', f'zero_{l}_finRingC'])
                self.match_finger(finger_joints=[f'pinky_01_{l}', f'pinky_02_{l}', f'pinky_03_{l}'],
                                  zero_joints=[f'zero_{l}_finPinkyA', f'zero_{l}_finPinkyB', f'zero_{l}_finPinkyC'])
                if not cmds.objExists('upperarm_r'):
                    upperarm_l_parent = cmds.listRelatives('upperarm_l', parent=True)
                    cmds.parent('upperarm_l', world=True)

                    cmds.mirrorJoint('upperarm_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=("_l", "_r"))
                    self.safe_parent('upperarm_l', upperarm_l_parent)

        #导入腿
        side=self.side_list
        for l in side:
            if not cmds.objExists(f'thigh_{l}'):
                cmds.warning(f'没有找到thigh_{l}')
            else:
                # 判断是否导入了文件
                if not cmds.objExists(f'grp_{l}_leg'):
                    if self.current_index==0:
                        self.import_file(f'controls_{l}_leg')
                    elif self.current_index==1:
                        self.import_file(f'controls_{l}_legUE')
                self.safe_parent(f'grp_{l}_leg', 'ctrl_c_root')

                # 左腿ik
                cmds.matchTransform(f'zero_{l}_footIk', f'foot_{l}', position=True)
                cmds.matchTransform(f'ctrl_{l}_footIk', f'foot_{l}', rotation=True)
                c = [f'zero_{l}_footHeel', f'zero_{l}_footPivot', f'jnt_{l}_heelPivot']
                cmds.parent(c, world=True)
                self.freeze_transform(f'ctrl_{l}_footIk')
                self.safe_parent(c, f'ctrl_{l}_footIk')
                cmds.matchTransform(f'jnt_{l}_heelPivot', f'heelPivot_{l}')
                cmds.matchTransform(f'jnt_{l}_heel', f'heel_{l}')
                cmds.matchTransform(f'jnt_{l}_footPivot', f'footPivot_{l}')
                cmds.matchTransform(f'jnt_{l}_toeFrontPivot', f'toeFrontPivot_{l}')
                cmds.matchTransform(f'jnt_{l}_footOutPivot', f'footOutPivot_{l}')
                cmds.matchTransform(f'jnt_{l}_footInPivot', f'footInPivot_{l}')
                cmds.matchTransform(f'jnt_{l}_toePivot', f'ball_{l}',position=True)
                cmds.matchTransform(f'jnt_{l}_ballFoot', f'foot_{l}',position=True)
                cmds.matchTransform(f'zero_{l}_footPivot',f'toeFrontPivot_{l}')

                cmds.matchTransform(f'jnt_{l}_thighIk', f'thigh_{l}')
                cmds.matchTransform(f'jnt_{l}_shinIk', f'calf_{l}')
                cmds.matchTransform(f'jnt_{l}_footIk', f'foot_{l}')
                cmds.matchTransform(f'jnt_{l}_toeIk', f'ball_{l}')
                self.freeze_transform([f'jnt_{l}_thighIk', f'jnt_{l}_shinIk', f'jnt_{l}_footIk', f'jnt_{l}_toeIk'])

                self.safe_parent(f'zero_{l}_legPv', f'jnt_{l}_shinIk')
                max_axis,up_axis=self.max_joint_orient(f'jnt_{l}_shinIk')
                cmds.xform(f'zero_{l}_legPv', translation=[0, 0, 0])
                rate = cmds.getAttr(f'calf_{l}.tx') / 45.7

                cmds.setAttr(f'zero_{l}_legPv.t{up_axis}', 63 * rate)
                self.safe_parent(f'zero_{l}_legPv', f'grp_{l}_legIk')

                # 左腿fk
                cmds.matchTransform(f'zero_{l}_thighFk', f'thigh_{l}')
                cmds.matchTransform(f'zero_{l}_shinFk', f'calf_{l}')
                cmds.matchTransform(f'zero_{l}_footFk', f'foot_{l}')
                cmds.matchTransform(f'zero_{l}_toe', f'ball_{l}')

                cmds.setAttr(f"crv_{l}_legFkPv.translateX", lock=False)
                cmds.setAttr(f"crv_{l}_legFkPv.translateY", lock=False)
                cmds.setAttr(f"crv_{l}_legFkPv.translateZ", lock=False)
                cmds.setAttr(f"crv_{l}_legFkPv.rotateX", lock=False)
                cmds.setAttr(f"crv_{l}_legFkPv.rotateY", lock=False)
                cmds.setAttr(f"crv_{l}_legFkPv.rotateZ", lock=False)
                cmds.matchTransform(f'crv_{l}_legFkPv', f'ctrl_{l}_legPv')

                self.safe_parent(f'zero_{l}_legIkFkText', f'calf_{l}')
                cmds.xform(f'zero_{l}_legIkFkText',translation=[0,0,0],rotation=[0,0,0])
                cmds.setAttr(f'zero_{l}_legIkFkText.tx',20 * rate)
                cmds.setAttr(f'zero_{l}_legIkFkText.t{max_axis}', 7 * rate)

                cmds.setAttr(f'zero_{l}_legIkFkText.r{up_axis}', 90)
                if max_axis=='z':
                    cmds.setAttr(f'zero_{l}_legIkFkText.rx', 90)
                self.safe_parent(f'zero_{l}_legIkFkText', f'grp_{l}_leg')

                if not cmds.objExists('thigh_r'):
                    cmds.mirrorJoint('thigh_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=("_l", "_r"))
                if not cmds.objExists('heelPivot_r'):
                    cmds.mirrorJoint('heelPivot_l', mirrorYZ=True, mirrorBehavior=True, searchReplace=("_l", "_r"))

    '''
    对齐手指
    '''
    def match_finger(self,finger_joints,zero_joints):
        for finger_joint, zero_joint in zip(finger_joints, zero_joints):
            if cmds.objExists(finger_joint):
                cmds.matchTransform(zero_joint, finger_joint)
            else:
                cmds.delete(zero_joint)
                break

        
    '''
    创建简单链
    '''
    def simple_chain(self):
        selection_objs = cmds.ls(selection=True)
        last_ctrl = None
        first_iteration = True
        for obj in selection_objs:
            parts = obj.split('_')
            name = parts[0]
            number = parts[1]
            side = parts[2] if len(parts) > 2 else 'c'
            
            zero = cmds.createNode('transform',name=f'zero_{side}_{name}_{number}')
            if last_ctrl:
                cmds.parent(zero,last_ctrl)
            driven = cmds.createNode('transform',name=f'driven_{side}_{name}_{number}')
            
            if first_iteration:
                rate=1
                first_iteration = False
            else:
                rate = cmds.getAttr(obj+'.tx')/15
            
            ctrl = cmds.circle(radius=5*rate, nr=(0, 1, 0), c=(0, 0, 0),name=f'ctrl_{side}_{name}_{number}')[0]

            cmds.select(ctrl)
            cmds.DeleteHistory()
            cmds.parent(ctrl,driven)
            cmds.parent(driven,zero)
            cmds.matchTransform(zero,obj)
            cmds.setAttr(ctrl+'.rz',90)
            self.freeze_transform(ctrl)
            axials=['x','y','z']
            for a in axials:
                cmds.setAttr(f'{ctrl}.s{a}',lock=True,keyable=False)
            cmds.setAttr(ctrl+'.v',keyable=False)
            last_ctrl = ctrl
            if cmds.objExists('ctrl_c_root'):
                cmds.addAttr(ctrl,attributeType='float', longName='rotateFollow',maxValue=1, minValue=0,keyable=True,niceName='旋转跟随')
                pc_name = self.parentCon(['ctrl_c_root',zero],driven,offset=True,skipTranslate=True)
                rev = cmds.createNode('reverse',name = f'rev_{side}_{name}_{number}')
                cmds.connectAttr(f'{ctrl}.rotateFollow',f'{pc_name}.zero_{side}_{name}_{number}W1')
                cmds.connectAttr(f'{ctrl}.rotateFollow',f'{rev}.inputX')
                cmds.connectAttr(f'{rev}.outputX',f'{pc_name}.ctrl_c_rootW0')
                
    '''
    父子约束
    '''
    def parentCon(self,parents,child,offset=False,skipTranslate=False, skipRotate=False,name=''):
        if name=='':
            name=f'{child}_parentConstraint_00'
        if skipTranslate:
            st=['x','y','z']
        else:
            st=[]
        if skipRotate:
            sr=['x','y','z']
        else:
            sr=[]
        conName = cmds.parentConstraint(parents, child, maintainOffset=offset, skipTranslate=st, skipRotate=sr,name=name)[0]
        cmds.setAttr(conName + '.interpType', 2)
        return name
    '''
    旋转约束
    '''
    def orientCon(self,parents,child,offset=False, skip=[],name=''):
        if name=='':
            name=f'{child}_orientConstraint_00'
        conName = cmds.orientConstraint(parents, child, maintainOffset=offset, skip=skip,name=name)[0]
        cmds.setAttr(conName + '.interpType', 2)
        return name
    '''
    位置约束
    '''
    def pointCon(self,parents,child,offset=False,skip=[],name=''):
        if name=='':
            name=f'{child}_pointConstraint_00'
        conName = cmds.pointConstraint(parents, child, maintainOffset=offset, skip=skip,name=name)[0]
        return name
    '''
    删除约束
    '''
    def deleteCon(self,obj):
        con = cmds.listRelatives(obj, children=True, type='constraint')
        self.safe_delete(con)
    '''
    高级设置属性
    '''
    def setAttrAdv(self,obj,attrs,value=None,channelBox=True,keyable=True,lock=False):
        for attr in attrs:
            if value==None:
                cmds.setAttr(f'{obj}.{attr}', channelBox=channelBox, keyable=keyable, lock=lock)
            else:
                cmds.setAttr(f'{obj}.{attr}',value,channelBox=channelBox,keyable=keyable,lock=lock)
    '''
    获取骨骼朝向
    '''
    def get_direction(self,joint):
        # 获取物体的变换矩阵（4x4矩阵）
        matrix = cmds.xform(joint, query=True, matrix=True, worldSpace=True)

        # 将矩阵转换为MMatrix
        m_matrix = om.MMatrix(matrix)

        # 提取局部坐标系的各个轴向量
        local_x = om.MVector(m_matrix[0], m_matrix[1], m_matrix[2])
        local_y = om.MVector(m_matrix[4], m_matrix[5], m_matrix[6])
        local_z = om.MVector(m_matrix[8], m_matrix[9], m_matrix[10])

        # 定义世界坐标轴
        world_x = om.MVector(1, 0, 0)
        world_y = om.MVector(0, 1, 0)
        world_z = om.MVector(0, 0, 1)

        # 初始化结果列表
        result = []

        # 计算世界坐标轴 X、Y、Z 在局部坐标系中的方向
        # 世界 X 轴
        world_x = om.MVector(1, 0, 0)
        axes_x = [('x', local_x * world_x), ('y', local_y * world_x), ('z', local_z * world_x)]
        max_axis_x = max(axes_x, key=lambda item: abs(item[1]))
        result.append(max_axis_x[0] if max_axis_x[1] > 0 else f"-{max_axis_x[0]}")

        # 世界 Y 轴
        world_y = om.MVector(0, 1, 0)
        axes_y = [('x', local_x * world_y), ('y', local_y * world_y), ('z', local_z * world_y)]
        max_axis_y = max(axes_y, key=lambda item: abs(item[1]))
        result.append(max_axis_y[0] if max_axis_y[1] > 0 else f"-{max_axis_y[0]}")

        # 世界 Z 轴
        world_z = om.MVector(0, 0, 1)
        axes_z = [('x', local_x * world_z), ('y', local_y * world_z), ('z', local_z * world_z)]
        max_axis_z = max(axes_z, key=lambda item: abs(item[1]))
        result.append(max_axis_z[0] if max_axis_z[1] > 0 else f"-{max_axis_z[0]}")

        return result
    '''
    获取最大位移轴
    '''
    def get_max_translate(self,joint):
        t=cmds.xform(joint,q=True,translation=True)
        # 创建一个包含绝对值和对应轴名的列表
        axis = [('x', t[0]), ('y', t[1]), ('z', t[2])]

        # 找到绝对值最大的轴
        max_axis = max(axis, key=lambda item: abs(item[1]))

        # 根据符号返回正负方向
        return max_axis[0] if max_axis[1] > 0 else f"-{max_axis[0]}"
    '''
    获取两者之间的距离
    '''
    def get_distance(self,obj1, obj2):
        # 获取物体的位置
        pos1 = cmds.xform(obj1, query=True, translation=True, worldSpace=True)
        pos2 = cmds.xform(obj2, query=True, translation=True, worldSpace=True)

        # 计算两点之间的距离
        distance = math.sqrt(
            (pos2[0] - pos1[0]) ** 2 +
            (pos2[1] - pos1[1]) ** 2 +
            (pos2[2] - pos1[2]) ** 2
        )

        return distance
    '''
    判断是否导入控制器
    '''
    def rig(self):
        if cmds.objExists('ctrl_c_root'):
            self.finish_rig()
        else:
            cmds.warning('请先创建控制器')
    '''
    完成绑定！
    '''
    def finish_rig(self):
        cmds.undoInfo(openChunk=True)
        self.safe_delete(['heelPivot_l','heelPivot_r'])
        last_spine = cmds.listRelatives('neck_01', parent=True)[0]
        last_neck = cmds.listRelatives('head', parent=True)[0]
        #躯干ik
        if cmds.objExists('jnt_c_spineA') and cmds.objExists('jnt_c_neck'):
            cmds.setAttr('jnt_c_spineA.v',False)
            spine_max_translate = self.get_max_translate('spine_02')
            spine_direction = self.get_direction('spine_01')
            spine_translate_map = {
                'x': 0,
                '-x': 1,
                'y': 2,
                '-y': 3,
                'z': 4,
                '-z': 5
            }

            # 使用字典来映射 spine_direction 的值
            spine_direction_map = {
                'y': 0,
                '-y': 1,
                'z': 3,
                '-z': 4,
                'x': 6,
                '-x': 7
            }

            # 获取 spine_max_translate 的映射值
            fa = spine_translate_map.get(spine_max_translate)

            # 获取 spine_direction[2] 的映射值
            ua = spine_direction_map.get(spine_direction[2])

            spineik_handle = cmds.ikHandle(
                startJoint='jnt_c_spineA',
                endEffector='jnt_c_neck',
                solver='ikSplineSolver',
                createCurve=False,
                parentCurve=False,
                curve='crv_c_spine',
                name='ikHandle_spine'
            )
            cmds.rename(spineik_handle[1], 'effector_spine')
            cmds.parent('ikHandle_spine', 'grp_c_spineIk')
            cmds.setAttr("ikHandle_spine.v", False)
            cmds.setAttr("crv_c_spine.v", False)
            cmds.setAttr("ikHandle_spine.dTwistControlEnable", True)
            cmds.setAttr("ikHandle_spine.dWorldUpType", 4)
            cmds.setAttr("ikHandle_spine.dForwardAxis", fa)
            cmds.setAttr("ikHandle_spine.dWorldUpAxis", ua)
            cmds.setAttr("ikHandle_spine.dWorldUpVectorX", 0)
            cmds.setAttr("ikHandle_spine.dWorldUpVectorY", 0)
            cmds.setAttr("ikHandle_spine.dWorldUpVectorZ", 1)
            cmds.setAttr("ikHandle_spine.dWorldUpVectorEndX", 0)
            cmds.setAttr("ikHandle_spine.dWorldUpVectorEndY", 0)
            cmds.setAttr("ikHandle_spine.dWorldUpVectorEndZ", 1)
            cmds.connectAttr('output_c_cog.worldMatrix','ikHandle_spine.dWorldUpMatrix',f=True)
            cmds.connectAttr('output_c_spineIk.worldMatrix','ikHandle_spine.dWorldUpMatrixEnd',f=True)

        # 脖子ik
        if cmds.objExists('jnt_c_neckA') and cmds.objExists('jnt_c_head'):
            neckik_handle = cmds.ikHandle(
                startJoint='jnt_c_neckA',
                endEffector='jnt_c_head',
                solver='ikSplineSolver',
                createCurve=False,
                parentCurve=False,
                curve='crv_c_neck',
                name='ikHandle_neck'
            )
            cmds.rename(neckik_handle[1], 'effector_neck')
            cmds.parent('ikHandle_neck', 'grp_c_neckIk')
            cmds.setAttr("ikHandle_neck.v", False)
            cmds.setAttr("ikHandle_neck.dTwistControlEnable", True)
            cmds.setAttr("ikHandle_neck.dWorldUpType", 4)
            cmds.setAttr("ikHandle_neck.dForwardAxis", 2)
            cmds.setAttr("ikHandle_neck.dWorldUpAxis", 3)
            cmds.setAttr("ikHandle_neck.dWorldUpVectorX", 0)
            cmds.setAttr("ikHandle_neck.dWorldUpVectorY", 0)
            cmds.setAttr("ikHandle_neck.dWorldUpVectorZ", 1)
            cmds.setAttr("ikHandle_neck.dWorldUpVectorEndX", 0)
            cmds.setAttr("ikHandle_neck.dWorldUpVectorEndY", 0)
            cmds.setAttr("ikHandle_neck.dWorldUpVectorEndZ", 1)
            cmds.connectAttr(f'{last_spine}.worldMatrix', 'ikHandle_neck.dWorldUpMatrix',f=True)
            cmds.connectAttr('output_c_headIk.worldMatrix', 'ikHandle_neck.dWorldUpMatrixEnd',f=True)

        #创建约束
        #躯干约束
        if cmds.objExists('crv_c_spine'):
            cmds.setAttr('crv_c_spine.inheritsTransform',False)
        if cmds.objExists('crv_c_neck'):
            cmds.setAttr('crv_c_neck.inheritsTransform', False)
        if cmds.objExists('crv_c_tail'):
            cmds.setAttr('crv_c_tail.inheritsTransform', False)
        if cmds.objExists('root'):
            self.parentCon('ctrl_c_rootFollow','root',offset=True)
            cmds.scaleConstraint('ctrl_c_rootFollow','root',maintainOffset=True)
        self.parentCon('output_c_cog','pelvis',offset=True,name='pelvis_parentConstraint_00')
        if cmds.objExists('grp_spinePoint'):
            self.parentCon('output_c_cog','jnt_c_spineIkA',name='jnt_c_spineIkA_parentConstraint_00')
            self.parentCon('output_c_spineIk','jnt_c_neckIk',name='jnt_c_neckIk_parentConstraint_00')
        # spineIk空间切换
        self.parentCon(['ctrl_c_root', 'output_c_cog'], 'driven_c_spineIk', offset=True)
        cmds.connectAttr('con_c_spineIk_00.outColorR', 'driven_c_spineIk_parentConstraint_00.ctrl_c_rootW0', f=True)
        cmds.connectAttr('con_c_spineIk_01.outColorR', 'driven_c_spineIk_parentConstraint_00.output_c_cogW1', f=True)
        
        spine_index = 1
        current_spine = 'spine_01'
        last_spine_reached = False
        first_loop=True
        while current_spine:
            ctrl_spineFk = f'ctrl_c_spine{chr(64 + spine_index)}'  # A, B, C... 代表关节
            joint_spineIk = f'jnt_c_spine{chr(64 + spine_index)}'
            constraint_spine = f'{current_spine}_parentConstraint_00'
            zero_spineFk = f'zero_c_spine{chr(64 + spine_index)}'
            driven_spineFk = f'driven_c_spine{chr(64 + spine_index)}'
            driven_spineFk_con = f'{driven_spineFk}_parentConstraint_00'

            driven_spineIk = f'driven_c_spineIk{chr(64 + spine_index)}'
            #旋转跟随
            self.parentCon([zero_spineFk,'ctrl_c_root'],driven_spineFk,offset=True,skipTranslate=True,name=driven_spineFk_con)
            if not cmds.objExists(f'rev_{ctrl_spineFk}'):
                cmds.createNode('reverse',name=f'rev_{ctrl_spineFk}')
            cmds.connectAttr(f'{ctrl_spineFk}.rotateFollow',f'{driven_spineFk_con}.{zero_spineFk}W0',f=True)
            cmds.connectAttr(f'{ctrl_spineFk}.rotateFollow',f'rev_{ctrl_spineFk}.inputX',f=True)
            cmds.connectAttr(f'rev_{ctrl_spineFk}.outputX',f'{driven_spineFk_con}.ctrl_c_rootW1',f=True)
            #约束变形骨骼
            if cmds.objExists('jnt_c_spineA'):#如果存在spineIk
                if current_spine!=last_spine:#如果不是最后一节spine
                    self.parentCon([ctrl_spineFk,joint_spineIk],current_spine,offset=True,name=constraint_spine)
                    cmds.connectAttr('ctrl_c_cog.IKFK',f'{constraint_spine}.{ctrl_spineFk}W0',f=True)
                    cmds.connectAttr('rev_c_cog.outputX',f'{constraint_spine}.{joint_spineIk}W1',f=True)
                else:#如果是最后一节spine
                    self.parentCon([ctrl_spineFk, 'output_c_spineIk'], current_spine, offset=True, skipTranslate=True,name=constraint_spine)
                    cmds.connectAttr('ctrl_c_cog.IKFK', f'{constraint_spine}.{ctrl_spineFk}W0', f=True)
                    cmds.connectAttr('rev_c_cog.outputX', f'{constraint_spine}.output_c_spineIkW1', f=True)

                if not first_loop and cmds.objExists(driven_spineIk):
                    self.parentCon(['output_c_cog','output_c_spineIk'],driven_spineIk,offset=True,name=f'{driven_spineIk}_parentConstraint_00')

                    a=self.get_distance('spine_01',current_spine)
                    b=self.get_distance('spine_01','neck_01')
                    weight_a=a/b
                    weight_b=1-weight_a
                    cmds.setAttr(f'{driven_spineIk}_parentConstraint_00.output_c_cogW0',weight_b)
                    cmds.setAttr(f'{driven_spineIk}_parentConstraint_00.output_c_spineIkW1', weight_a)

                self.parentCon(last_spine,'crv_c_spineFk',offset=True)

            else:#如果不存在spineIk
                self.parentCon(ctrl_spineFk, current_spine, offset=True, name=constraint_spine)
                if cmds.attributeQuery('IKFK', node='ctrl_c_cog', exists=True):
                    cmds.deleteAttr('ctrl_c_cog.IKFK')
                if cmds.attributeQuery('IKFKVis', node='ctrl_c_cog', exists=True):
                    cmds.deleteAttr('ctrl_c_cog.IKFKVis')
            spine_index +=1
            current_spine = f'spine_{str(spine_index).zfill(2)}'
            first_loop = False
            if last_spine_reached:
                break  # 如果已经循环过last_spine，结束循环
            elif current_spine == last_spine:
                last_spine_reached = True  # 标记到达了last_spine
        
        
        self.parentCon(last_spine,'grp_c_spineC',offset=False,name='grp_c_spineC_parentConstraint_00')
        
        if cmds.objExists('clavicle_l'):
            self.parentCon('ctrl_l_shoulder','clavicle_l',offset=False,name='clavicle_l_parentConstraint_00')
        
        if cmds.objExists('clavicle_r'):
            self.parentCon('ctrl_r_shoulder','clavicle_r',offset=False,name='clavicle_r_parentConstraint_00')

        #脖子约束
        parts = last_neck.split('_')
        # 如果脖子骨骼数小于等于2
        if int(parts[1])<=2:
            #约束脖子和头蒙皮骨骼
            self.parentCon('ctrl_c_neck','neck_01',offset=False,name='neck_01_parentConstraint_00')
            self.parentCon('ctrl_c_head', 'head', offset=False)
            #脖子旋转跟随
            self.parentCon(['zero_c_neck','ctrl_c_root'],'driven_c_neck',offset=True,skipTranslate=True)
            self.safe_createNode('reverse',name='rev_neck')
            cmds.connectAttr('ctrl_c_neck.rotateFollow','driven_c_neck_parentConstraint_00.zero_c_neckW0')
            cmds.connectAttr('ctrl_c_neck.rotateFollow','rev_neck.inputX')
            cmds.connectAttr('rev_neck.outputX','driven_c_neck_parentConstraint_00.ctrl_c_rootW1')
            #头部旋转跟随
            self.parentCon(['zero_c_head', 'ctrl_c_root'], 'driven_c_head', offset=True, skipTranslate=True)
            self.safe_createNode('reverse', name='rev_head')
            cmds.connectAttr('ctrl_c_head.rotateFollow', 'driven_c_head_parentConstraint_00.zero_c_headW0')
            cmds.connectAttr('ctrl_c_head.rotateFollow', 'rev_head.inputX')
            cmds.connectAttr('rev_head.outputX', 'driven_c_head_parentConstraint_00.ctrl_c_rootW1')
            #如果存在neck_02
            if cmds.objExists('neck_02'):
                cmds.connectAttr('neck_01.rotate','neck_02.rotate',f=True)
                self.parentCon('neck_02','driven_c_head',offset=True,skipRotate=True)
        else:#如果有脖子IK
            #添加脖子IKFK切换属性
            if not cmds.attributeQuery('neckIKFK', node='ctrl_c_cog', exists=True):
                cmds.addAttr('ctrl_c_cog', attributeType='float', defaultValue=1, maxValue=1, minValue=0,
                             longName='neckIKFK', niceName='脖子IKFK', keyable=True)
            if not cmds.attributeQuery('neckIKFKVis', node='ctrl_c_cog', exists=True):
                cmds.addAttr('ctrl_c_cog', longName='neckIKFKVis',attributeType='bool', defaultValue=False, niceName='脖子IKFK切换显示')
                cmds.setAttr('ctrl_c_cog.neckIKFKVis', keyable=False, channelBox=True)
            self.safe_createNode('reverse',name='rev_c_neckIkFk')
            cmds.connectAttr('ctrl_c_cog.neckIKFK','rev_c_neckIkFk.inputX',f=True)
            cmds.connectAttr('ctrl_c_cog.neckIKFKVis','rev_c_neckIkFk.inputY',f=True)
            self.safe_createNode('addDoubleLinear',name='add_c_neckIk')
            self.safe_createNode('addDoubleLinear', name='add_c_neckFk')
            cmds.connectAttr('rev_c_neckIkFk.outputX','add_c_neckIk.input1',f=True)
            cmds.connectAttr('rev_c_neckIkFk.outputY','add_c_neckIk.input2',f=True)
            cmds.connectAttr('ctrl_c_cog.neckIKFK', 'add_c_neckFk.input1', f=True)
            cmds.connectAttr('rev_c_neckIkFk.outputY', 'add_c_neckFk.input2', f=True)
            cmds.connectAttr('add_c_neckFk.output','zero_c_neckA.v',f=True)
            cmds.connectAttr('add_c_neckIk.output','grp_c_neckIk.v',f=True)
            #约束IK控制器
            self.parentCon(last_spine,'driven_c_neckIkA',offset=True,name='driven_c_neckIkA_parentConstraint_00')

            self.parentCon('output_c_headIk','jnt_c_headIk',offset=False,name='jnt_c_headIk_parentConstraint_00')
            neck_index = 1
            current_neck = 'neck_01'
            last_neck_reached = False
            first_loop=True
            while current_neck:
                ctrl_name = f'ctrl_c_neck{chr(64 + neck_index)}'  # A, B, C... 代表关节
                joint_name = f'jnt_c_neck{chr(64 + neck_index)}'
                constraint_name = f'{current_neck}_parentConstraint_00'
                driven_neckIk = f'driven_c_neckIk{chr(64 + neck_index)}'

                self.parentCon([ctrl_name, joint_name], current_neck, offset=True, name=constraint_name)
                cmds.connectAttr('ctrl_c_cog.neckIKFK', f'{constraint_name}.{ctrl_name}W0', f=True)
                if not cmds.objExists(f'rev_{current_neck}'):
                    cmds.createNode('reverse', name=f'rev_{current_neck}')
                cmds.connectAttr('ctrl_c_cog.neckIKFK', f'rev_{current_neck}.inputX', f=True)
                cmds.connectAttr(f'rev_{current_neck}.outputX', f'{constraint_name}.{joint_name}W1', f=True)

                if not first_loop and cmds.objExists(driven_neckIk):
                    self.parentCon([last_spine,'output_c_headIk'],driven_neckIk,offset=True,name=f'{driven_neckIk}_parentConstraint_00')
                    a = self.get_distance('neck_01', current_neck)
                    b = self.get_distance('head', 'neck_01')
                    weight_a = a / b
                    weight_b = 1 - weight_a
                    cmds.setAttr(f'{driven_neckIk}_parentConstraint_00.{last_spine}W0', weight_b)
                    cmds.setAttr(f'{driven_neckIk}_parentConstraint_00.output_c_headIkW1', weight_a)
                neck_index += 1
                current_neck = f'neck_{str(neck_index).zfill(2)}'
                first_loop=False
                if last_neck_reached:
                    break  # 如果已经循环过last_neck，结束循环
                elif current_neck == last_neck:
                    last_neck_reached = True  # 标记到达了last_neck
                self.parentCon(['ctrl_c_head','output_c_headIk'],'head',offset=True,skipTranslate=True,name='head_parentConstraint_00')

            if not cmds.objExists('rev_ctrl_c_head'):
                cmds.createNode('reverse',name='rev_ctrl_c_head')
            cmds.connectAttr('ctrl_c_cog.neckIKFK','head_parentConstraint_00.ctrl_c_headW0',f=True)
            cmds.connectAttr('ctrl_c_cog.neckIKFK','rev_ctrl_c_head.inputX',f=True)
            cmds.connectAttr('rev_ctrl_c_head.outputX','head_parentConstraint_00.output_c_headIkW1',f=True)
            #头部空间切换
            self.parentCon(['ctrl_c_root',last_spine],'driven_c_headIk',offset=True)
            cmds.connectAttr('con_c_headIk_00.outColorR','driven_c_headIk_parentConstraint_00.ctrl_c_rootW0')
            cmds.connectAttr('con_c_headIk_01.outColorR',f'driven_c_headIk_parentConstraint_00.{last_spine}W1')
        #胳膊
        arm_side=self.side_list
        for l in arm_side:
            if cmds.objExists(f'upperarm_{l}'):
                #创建手臂IK
                arm_l_ik_handle = cmds.ikHandle(
                    startJoint=f'jnt_{l}_upperarmIk',
                    endEffector=f'jnt_{l}_handIk',
                    name=f'ikHandle_{l}_hand'
                )
                cmds.rename(arm_l_ik_handle[1], f'effector_{l}_hand')
                cmds.parent(f'ikHandle_{l}_hand', f'ctrl_{l}_handIk')
                cmds.setAttr(f'ikHandle_{l}_hand.v', False)
                cmds.setAttr(f'jnt_{l}_upperarmIk.v', False)
                cmds.poleVectorConstraint(f'ctrl_{l}_armPv', f'ikHandle_{l}_hand')

                #肩膀约束大臂
                self.parentCon(f'ctrl_{l}_shoulder', f'jnt_{l}_upperarmIk', offset=True,skipRotate=True, name=f'jnt_{l}_upperarmIk_parentConstraint_00')
                self.parentCon(f'ctrl_{l}_shoulder', f'driven_{l}_upperarmFk', offset=True,skipRotate=True, name=f'driven_{l}_upperarmFk_parentConstraint_00')
                self.parentCon([f'ctrl_{l}_shoulder', 'ctrl_c_root'], f'driven_{l}_upperarmFk', offset=True,skipTranslate=True, name=f'driven_{l}_upperarmFk_parentConstraint_01')
                #大臂FK旋转跟随
                cmds.connectAttr(f'ctrl_{l}_upperarmFk.rotateFollow',f'driven_{l}_upperarmFk_parentConstraint_01.ctrl_{l}_shoulderW0', f=True)
                self.safe_createNode('reverse', name=f'reverse_driven_{l}_upperarmFk')
                cmds.connectAttr(f'ctrl_{l}_upperarmFk.rotateFollow', f'reverse_driven_{l}_upperarmFk.inputX', f=True)
                cmds.connectAttr(f'reverse_driven_{l}_upperarmFk.outputX',f'driven_{l}_upperarmFk_parentConstraint_01.ctrl_c_rootW1', f=True)
                #IKFK分别约束蒙皮骨骼
                self.orientCon([f'jnt_{l}_upperarmIk', f'output_{l}_upperarmFk'], f'upperarm_{l}', offset=False,name=f'upperarm_{l}_orientConstraint_00')
                self.orientCon([f'jnt_{l}_forearmIk', f'ctrl_{l}_forearmFk'], f'lowerarm_{l}', offset=False,name=f'lowerarm_{l}_orientConstraint_00')
                self.orientCon([f'ctrl_{l}_handIk', f'ctrl_{l}_handFk'], f'hand_{l}', offset=False,name=f'hand_{l}_orientConstraint_00')
                #IKFK融合连接
                cmds.connectAttr(f'rem_{l}_armBlendIkFk.outValue',f'upperarm_{l}_orientConstraint_00.jnt_{l}_upperarmIkW0', f=True)
                cmds.connectAttr(f'rem_{l}_armBlendIkFk.outValue', f'lowerarm_{l}_orientConstraint_00.jnt_{l}_forearmIkW0',f=True)
                cmds.connectAttr(f'rem_{l}_armBlendIkFk.outValue', f'hand_{l}_orientConstraint_00.ctrl_{l}_handIkW0', f=True)
                cmds.connectAttr(f'rev_{l}_armBlendIkFk.outputX', f'upperarm_{l}_orientConstraint_00.output_{l}_upperarmFkW1',f=True)
                cmds.connectAttr(f'rev_{l}_armBlendIkFk.outputX', f'lowerarm_{l}_orientConstraint_00.ctrl_{l}_forearmFkW1',f=True)
                cmds.connectAttr(f'rev_{l}_armBlendIkFk.outputX', f'hand_{l}_orientConstraint_00.ctrl_{l}_handFkW1', f=True)
                #约束IKFK切换控制器
                self.parentCon(f'lowerarm_{l}',f'driven_{l}_armIkFkText',offset=True)
                # 空间切换
                self.parentCon(['ctrl_c_root', 'output_c_cog', last_spine, 'head'], f'driven_{l}_handIk', offset=True)
                cmds.connectAttr(f'con_{l}_handIk_00.outColorR', f'driven_{l}_handIk_parentConstraint_00.ctrl_c_rootW0', f=True)
                cmds.connectAttr(f'con_{l}_handIk_01.outColorR', f'driven_{l}_handIk_parentConstraint_00.output_c_cogW1', f=True)
                cmds.connectAttr(f'con_{l}_handIk_02.outColorR', f'driven_{l}_handIk_parentConstraint_00.{last_spine}W2', f=True)
                cmds.connectAttr(f'con_{l}_handIk_03.outColorR', f'driven_{l}_handIk_parentConstraint_00.headW3', f=True)

                self.parentCon(['ctrl_c_root', 'output_c_cog'], f'driven_{l}_armPv', offset=True)
                cmds.connectAttr(f'con_{l}_armPv_00.outColorR', f'driven_{l}_armPv_parentConstraint_00.ctrl_c_rootW0', f=True)
                cmds.connectAttr(f'con_{l}_armPv_01.outColorR', f'driven_{l}_armPv_parentConstraint_00.output_c_cogW1', f=True)

                # 手指
                self.parentCon(f'hand_{l}', f'grp_{l}_finger', offset=False,name=f'grp_{l}_finger_parentConstraint_00')
                if cmds.objExists(f'pinky_metacarpal_{l}'):
                    self.parentCon(f'ctrl_{l}_finPinkyCarpal', f'pinky_metacarpal_{l}', offset=True,name=f'pinky_metacarpal_{l}_parentConstraint_00')
                if cmds.objExists(f'ring_metacarpal_{l}'):
                    self.parentCon([f'ctrl_{l}_finPinkyCarpal', f'grp_{l}_finger'],f'ring_metacarpal_{l}', offset=True,name=f'ring_metacarpal_{l}_parentConstraint_00')
                    cmds.setAttr(f'ring_metacarpal_{l}_parentConstraint_00.ctrl_{l}_finPinkyCarpalW0', 0.6)
                    cmds.setAttr(f'ring_metacarpal_{l}_parentConstraint_00.grp_{l}_fingerW1', 0.4)
                if cmds.objExists(f'middle_metacarpal_{l}'):
                    self.parentCon([f'ctrl_{l}_finPinkyCarpal', f'grp_{l}_finger'], f'middle_metacarpal_{l}', offset=True, name=f'middle_metacarpal_{l}_parentConstraint_00')
                    cmds.setAttr(f'middle_metacarpal_{l}_parentConstraint_00.ctrl_{l}_finPinkyCarpalW0', 0.3)
                    cmds.setAttr(f'middle_metacarpal_{l}_parentConstraint_00.grp_{l}_fingerW1', 0.7)
                if not cmds.objExists(f'pinky_metacarpal_{l}') and not cmds.objExists(f'ring_metacarpal_{l}') and not cmds.objExists(f'middle_metacarpal_{l}'):
                    self.safe_delete(f'zero_{l}_finPinkyCarpal')
                if cmds.objExists(f'driven_{l}_finPinkyA') and cmds.objExists(f'ctrl_{l}_finPinkyCarpal'):
                    if cmds.objExists(f'pinky_metacarpal_{l}'):
                        self.parentCon(f'pinky_metacarpal_{l}',f'driven_{l}_finPinkyA', offset=True,name=f'driven_{l}_finPinkyA_parentConstraint_00')
                    else:
                        self.parentCon(f'ctrl_{l}_finPinkyCarpal', f'driven_{l}_finPinkyA', offset=True,name=f'driven_{l}_finPinkyA_parentConstraint_00')

                if cmds.objExists(f'driven_{l}_finRingA') and cmds.objExists(f'ctrl_{l}_finPinkyCarpal'):
                    if cmds.objExists(f'ring_metacarpal_{l}'):
                        self.parentCon(f'ring_metacarpal_{l}',f'driven_{l}_finRingA', offset=True,name=f'driven_{l}_finRingA_parentConstraint_00')
                    else:
                        self.parentCon([f'ctrl_{l}_finPinkyCarpal', f'grp_{l}_finger'], f'driven_{l}_finRingA', offset=True,name=f'driven_{l}_finRingA_parentConstraint_00')
                        cmds.setAttr(f'driven_{l}_finRingA_parentConstraint_00.ctrl_{l}_finPinkyCarpalW0', 0.6)
                        cmds.setAttr(f'driven_{l}_finRingA_parentConstraint_00.grp_{l}_fingerW1', 0.4)

                if cmds.objExists(f'driven_{l}_finMidA') and cmds.objExists(f'ctrl_{l}_finPinkyCarpal'):
                    if cmds.objExists(f'middle_metacarpal_{l}'):
                        self.parentCon(f'middle_metacarpal_{l}',f'driven_{l}_finMidA', offset=True,name=f'driven_{l}_finMidA_parentConstraint_00')
                    else:
                        self.parentCon([f'ctrl_{l}_finPinkyCarpal', f'grp_{l}_finger'], f'driven_{l}_finMidA', offset=True,name=f'driven_{l}_finMidA_parentConstraint_00')
                        cmds.setAttr(f'driven_{l}_finMidA_parentConstraint_00.ctrl_{l}_finPinkyCarpalW0', 0.3)
                        cmds.setAttr(f'driven_{l}_finMidA_parentConstraint_00.grp_{l}_fingerW1', 0.7)

                if cmds.objExists(f'pinky_01_{l}'):
                    self.parentCon(f'ctrl_{l}_finPinkyA', f'pinky_01_{l}', offset=False,name=f'pinky_01_{l}_parentConstraint_00')
                if cmds.objExists(f'pinky_02_{l}'):
                    self.parentCon(f'ctrl_{l}_finPinkyB', f'pinky_02_{l}', offset=False,name=f'pinky_02_{l}_orientConstraint_00')
                if cmds.objExists(f'pinky_03_{l}'):
                    self.parentCon(f'ctrl_{l}_finPinkyC',f'pinky_03_{l}', offset=False,name=f'pinky_03_{l}_orientConstraint_00')
                if cmds.objExists(f'ring_01_{l}'):
                    self.parentCon(f'ctrl_{l}_finRingA', f'ring_01_{l}', offset=False,name=f'ring_01_{l}_parentConstraint_00')
                if cmds.objExists(f'ring_02_{l}'):
                    self.parentCon(f'ctrl_{l}_finRingB', f'ring_02_{l}', offset=False,name=f'ring_02_{l}_orientConstraint_00')
                if cmds.objExists(f'ring_03_{l}'):
                    self.parentCon(f'ctrl_{l}_finRingC', f'ring_03_{l}', offset=False,name=f'ring_03_{l}_orientConstraint_00')
                if cmds.objExists(f'middle_01_{l}'):
                    self.parentCon(f'ctrl_{l}_finMidA', f'middle_01_{l}', offset=False,name=f'middle_01_{l}_parentConstraint_00')
                if cmds.objExists(f'middle_02_{l}'):
                    self.parentCon(f'ctrl_{l}_finMidB', f'middle_02_{l}', offset=False,name=f'middle_02_{l}_orientConstraint_00')
                if cmds.objExists(f'middle_03_{l}'):
                    self.parentCon(f'ctrl_{l}_finMidC', f'middle_03_{l}', offset=False,name=f'middle_03_{l}_orientConstraint_00')
                if cmds.objExists(f'index_01_{l}'):
                    self.parentCon(f'ctrl_{l}_finIndexA', f'index_01_{l}', offset=False,name=f'index_01_{l}_parentConstraint_00')
                if cmds.objExists(f'index_02_{l}'):
                    self.parentCon(f'ctrl_{l}_finIndexB', f'index_02_{l}', offset=False, name=f'index_02_{l}_orientConstraint_00')
                if cmds.objExists(f'index_03_{l}'):
                    self.parentCon(f'ctrl_{l}_finIndexC', f'index_03_{l}', offset=False,name=f'index_03_{l}_orientConstraint_00')
                if cmds.objExists(f'thumb_01_{l}'):
                    self.parentCon(f'ctrl_{l}_finThumbA', f'thumb_01_{l}', offset=False,name=f'thumb_01_{l}_parentConstraint_00')
                if cmds.objExists(f'thumb_02_{l}'):
                    self.parentCon(f'ctrl_{l}_finThumbB', f'thumb_02_{l}', offset=False,name=f'thumb_02_{l}_orientConstraint_00')
                if cmds.objExists(f'thumb_03_{l}'):
                    self.parentCon(f'ctrl_{l}_finThumbC', f'thumb_03_{l}', offset=False,name=f'thumb_03_{l}_orientConstraint_00')

        #腿约束
        leg_side = self.side_list
        for l in leg_side:
            if cmds.objExists(f'thigh_{l}'):
                #腿部IK
                leg_l_ik_handle = cmds.ikHandle(
                    startJoint=f'jnt_{l}_thighIk',
                    endEffector=f'jnt_{l}_footIk',
                    name=f'ikHandle_{l}_foot'
                )
                cmds.rename(leg_l_ik_handle[1], f'effector_{l}_foot')
                cmds.parent(f'ikHandle_{l}_foot', f'jnt_{l}_ballFoot')
                cmds.setAttr(f'ikHandle_{l}_foot.v', False)
                cmds.poleVectorConstraint(f'ctrl_{l}_legPv', f'ikHandle_{l}_foot')
                # 左脚趾ik
                toe_l_ik_handle = cmds.ikHandle(
                    startJoint=f'jnt_{l}_footIk',
                    endEffector=f'jnt_{l}_toeIk',
                    solver='ikSCsolver',
                    name=f'ikHandle_{l}_toe'
                )
                cmds.rename(toe_l_ik_handle[1], f'effector_{l}_toe')
                cmds.parent(f'ikHandle_{l}_toe', f'jnt_{l}_toePivot')
                cmds.setAttr(f'ikHandle_{l}_toe.v', False)

                cmds.setAttr(f'jnt_{l}_heelPivot.v', False)
                cmds.setAttr(f'jnt_{l}_thighIk.v',False)
                # 重心约束大腿
                self.parentCon('output_c_cog', f'jnt_{l}_thighIk', offset=True, skipRotate=True)

                self.parentCon('output_c_cog', f'driven_{l}_thighFk', offset=True, skipRotate=True,name=f'driven_{l}_thighFk_parentConstraint_00')
                self.parentCon(['output_c_cog', 'ctrl_c_root'], f'driven_{l}_thighFk', offset=True, skipTranslate=True,name=f'driven_{l}_thighFk_parentConstraint_01')

                cmds.connectAttr(f'ctrl_{l}_thighFk.rotateFollow', f'driven_{l}_thighFk_parentConstraint_01.output_c_cogW0', f=True)
                self.safe_createNode('reverse', name=f'rev_{l}_thighFk')
                cmds.connectAttr(f'ctrl_{l}_thighFk.rotateFollow', f'rev_{l}_thighFk.inputX', f=True)
                cmds.connectAttr(f'rev_{l}_thighFk.outputX', f'driven_{l}_thighFk_parentConstraint_01.ctrl_c_rootW1', f=True)

                # 脚趾
                self.parentCon(f'ctrl_{l}_toe', f'ball_{l}', offset=False)
                self.parentCon(f'foot_{l}', f'driven_{l}_toe', offset=True, skipRotate=True)
                self.parentCon([f'jnt_{l}_footInPivot', f'ctrl_{l}_footFk'], f'driven_{l}_toe', offset=True, skipTranslate=True)
                cmds.connectAttr(f'rem_{l}_legBlendIkFk.outValue', f'driven_{l}_toe_parentConstraint_01.jnt_{l}_footInPivotW0', f=True)
                cmds.connectAttr(f'rev_{l}_legBlendIkFk.outputX', f'driven_{l}_toe_parentConstraint_01.ctrl_{l}_footFkW1', f=True)

                #脚尖
                self.parentCon(f'jnt_{l}_footPivot',f'driven_{l}_footPivot',offset=True)
                self.parentCon(f'ctrl_{l}_footPivot',f'jnt_{l}_toeFrontPivot')

                # 左腿
                self.orientCon([f'jnt_{l}_thighIk', f'ctrl_{l}_thighFk'], f'thigh_{l}', offset=False)
                self.orientCon([f'jnt_{l}_shinIk', f'ctrl_{l}_shinFk'], f'calf_{l}', offset=False)
                self.orientCon([f'jnt_{l}_footIk', f'ctrl_{l}_footFk'], f'foot_{l}', offset=False)

                cmds.connectAttr(f'rem_{l}_legBlendIkFk.outValue', f'thigh_{l}_orientConstraint_00.jnt_{l}_thighIkW0')
                cmds.connectAttr(f'rem_{l}_legBlendIkFk.outValue', f'calf_{l}_orientConstraint_00.jnt_{l}_shinIkW0')
                cmds.connectAttr(f'rem_{l}_legBlendIkFk.outValue', f'foot_{l}_orientConstraint_00.jnt_{l}_footIkW0')
                cmds.connectAttr(f'rev_{l}_legBlendIkFk.outputX', f'thigh_{l}_orientConstraint_00.ctrl_{l}_thighFkW1')
                cmds.connectAttr(f'rev_{l}_legBlendIkFk.outputX', f'calf_{l}_orientConstraint_00.ctrl_{l}_shinFkW1')
                cmds.connectAttr(f'rev_{l}_legBlendIkFk.outputX', f'foot_{l}_orientConstraint_00.ctrl_{l}_footFkW1')
                # IK空间切换
                self.parentCon(['ctrl_c_root', 'output_c_cog'], f'driven_{l}_footIk', offset=True)
                self.safe_createNode('reverse', name=f'rev_{l}_footIk')
                cmds.connectAttr(f'ctrl_{l}_footIk.space', f'driven_{l}_footIk_parentConstraint_00.output_c_cogW1', f=True)
                cmds.connectAttr(f'ctrl_{l}_footIk.space', f'rev_{l}_footIk.inputX', f=True)
                cmds.connectAttr(f'rev_{l}_footIk.outputX', f'driven_{l}_footIk_parentConstraint_00.ctrl_c_rootW0', f=True)
                # 极向量空间切换
                self.parentCon(['ctrl_c_root', 'output_c_cog'], f'driven_{l}_legPv', offset=True)
                self.safe_createNode('reverse', name=f'rev_{l}_legPv')
                cmds.connectAttr(f'ctrl_{l}_legPv.space', f'driven_{l}_legPv_parentConstraint_00.output_c_cogW1', f=True)
                cmds.connectAttr(f'ctrl_{l}_legPv.space', f'rev_{l}_legPv.inputX')
                cmds.connectAttr(f'rev_{l}_legPv.outputX', f'driven_{l}_legPv_parentConstraint_00.ctrl_c_rootW0', f=True)
                #IKFK混合约束
                self.parentCon(f'calf_{l}',f'driven_{l}_legIkFkText',offset=True)
        cmds.undoInfo(closeChunk=True)
    '''
    添加twist
    '''
    def create_twist(self):
        upperarmValue=self.spinBox_00.value()
        forearmValue = self.spinBox_01.value()
        thighValue = self.spinBox_02.value()
        shinValue = self.spinBox_03.value()
        side = self.side_list
        for l in side:
            if cmds.objExists(f'upperarm_{l}'):
                self.create_joint(name=f'jnt_{l}_upperarmTwist', parent=f'grp_{l}_armIk')
                self.create_joint(name=f'jnt_{l}_forearmTwist', parent=f'jnt_{l}_upperarmTwist')
                self.create_joint(name=f'jnt_{l}_handTwist', parent=f'jnt_{l}_forearmTwist')
                cmds.matchTransform(f'jnt_{l}_upperarmTwist', f'upperarm_{l}')
                cmds.matchTransform(f'jnt_{l}_forearmTwist', f'lowerarm_{l}')
                cmds.matchTransform(f'jnt_{l}_handTwist', f'hand_{l}')
                self.freeze_transform(name=[f'jnt_{l}_upperarmTwist', f'jnt_{l}_forearmTwist', f'jnt_{l}_handTwist'])
                # 左臂扭曲Ik
                upperarmTwist_l_ik_handle = cmds.ikHandle(
                    startJoint=f'jnt_{l}_upperarmTwist',
                    endEffector=f'jnt_{l}_forearmTwist',
                    solver='ikSCsolver',
                    name=f'ikHandle_{l}_upperarmTwist'
                )
                cmds.rename(upperarmTwist_l_ik_handle[1], f'effector_{l}_upperarmTwist')
                self.safe_parent(f'ikHandle_{l}_upperarmTwist', f'grp_{l}_armIk')
                cmds.setAttr(f'ikHandle_{l}_upperarmTwist.v', False)
                cmds.setAttr(f'jnt_{l}_upperarmTwist.v', False)
                forearmTwist_l_ik_handle = cmds.ikHandle(
                    startJoint=f'jnt_{l}_forearmTwist',
                    endEffector=f'jnt_{l}_handTwist',
                    solver='ikSCsolver',
                    name=f'ikHandle_{l}_forearmTwist'
                )
                cmds.rename(forearmTwist_l_ik_handle[1], f'effector_{l}_forearmTwist')
                self.safe_parent(f'ikHandle_{l}_forearmTwist', f'grp_{l}_armIk')
                cmds.setAttr(f'ikHandle_{l}_forearmTwist.v', False)

                # 创建约束
                self.parentCon(f'ctrl_{l}_shoulder', f'jnt_{l}_upperarmTwist', offset=True, skipRotate=True)

                self.parentCon(f'lowerarm_{l}', f'ikHandle_{l}_upperarmTwist', offset=True, skipRotate=True,name=f'ikHandle_{l}_upperarmTwist_parentConstraint_00')
                self.parentCon(f'ctrl_{l}_shoulder', f'ikHandle_{l}_upperarmTwist', offset=True, skipTranslate=True,name=f'ikHandle_{l}_upperarmTwist_parentConstraint_01')

                self.parentCon(f'hand_{l}', f'ikHandle_{l}_forearmTwist', offset=True)

                if upperarmValue!=0:
                    self.between_joints(f'upperarm_{l}',f'lowerarm_{l}','upperarm',f'upperarm_{l}',upperarmValue)
                    for upperarm in range(upperarmValue+1)[1:]:
                        weight_a = cmds.getAttr(f'upperarm_twist_{str(upperarm).zfill(2)}_{l}.translateX') / cmds.getAttr(f'lowerarm_{l}.translateX')
                        weight_b = 1 - weight_a

                        upperarm_orientCon = self.orientCon([f'upperarm_{l}', f'jnt_{l}_upperarmTwist'], f'upperarm_twist_{str(upperarm).zfill(2)}_{l}')
                        cmds.setAttr(f'{upperarm_orientCon}.upperarm_{l}W0', weight_a)
                        cmds.setAttr(f'{upperarm_orientCon}.jnt_{l}_upperarmTwistW1', weight_b)

                        upperarm_pointCon = self.pointCon([f'upperarm_{l}', f'lowerarm_{l}'], f'upperarm_twist_{str(upperarm).zfill(2)}_{l}')
                        cmds.setAttr(f'{upperarm_pointCon}.upperarm_{l}W0', weight_b)
                        cmds.setAttr(f'{upperarm_pointCon}.lowerarm_{l}W1', weight_a)
                if forearmValue != 0:
                    self.between_joints(f'hand_{l}',f'lowerarm_{l}','lowerarm',f'lowerarm_{l}',forearmValue)
                    for forearm in range(forearmValue+1)[1:]:
                        weight_a = cmds.getAttr(f'lowerarm_twist_{str(forearm).zfill(2)}_{l}.translateX') / cmds.getAttr(f'hand_{l}.translateX')
                        weight_b = 1 - weight_a

                        forearm_orientCon = self.orientCon([f'lowerarm_{l}', f'jnt_{l}_forearmTwist'], f'lowerarm_twist_{str(forearm).zfill(2)}_{l}')
                        cmds.setAttr(f'{forearm_orientCon}.lowerarm_{l}W0', weight_b)
                        cmds.setAttr(f'{forearm_orientCon}.jnt_{l}_forearmTwistW1', weight_a)

                        forearm_pointCon = self.pointCon([f'lowerarm_{l}', f'hand_{l}'], f'lowerarm_twist_{str(forearm).zfill(2)}_{l}')
                        cmds.setAttr(f'{forearm_pointCon}.lowerarm_{l}W0', weight_b)
                        cmds.setAttr(f'{forearm_pointCon}.hand_{l}W1', weight_a)

        side = self.side_list
        for l in side:
            if cmds.objExists(f'thigh_{l}'):
                self.create_joint(name=f'jnt_{l}_thighTwist', parent=f'grp_{l}_leg')
                self.create_joint(name=f'jnt_{l}_shinTwist', parent=f'jnt_{l}_thighTwist')
                self.create_joint(name=f'jnt_{l}_footTwist', parent=f'jnt_{l}_shinTwist')

                cmds.matchTransform(f'jnt_{l}_thighTwist', f'thigh_{l}')
                cmds.matchTransform(f'jnt_{l}_shinTwist', f'calf_{l}')
                cmds.matchTransform(f'jnt_{l}_footTwist',f'foot_{l}')
                self.freeze_transform(name=[f'jnt_{l}_thighTwist', f'jnt_{l}_shinTwist', f'jnt_{l}_footTwist'])

                # 左腿扭曲Ik
                thighTwist_l_ik_handle = cmds.ikHandle(
                    startJoint=f'jnt_{l}_thighTwist',
                    endEffector=f'jnt_{l}_shinTwist',
                    solver='ikSCsolver',
                    name=f'ikHandle_{l}_thighTwist'
                )
                cmds.rename(thighTwist_l_ik_handle[1], f'effector_{l}_thighTwist')
                cmds.parent(f'ikHandle_{l}_thighTwist', f'grp_{l}_leg')
                cmds.setAttr(f'ikHandle_{l}_thighTwist.v', False)
                cmds.setAttr(f'jnt_{l}_thighTwist.v', False)
                shinTwist_l_ik_handle = cmds.ikHandle(
                    startJoint=f'jnt_{l}_shinTwist',
                    endEffector=f'jnt_{l}_footTwist',
                    solver='ikSCsolver',
                    name=f'ikHandle_{l}_shinTwist'
                )
                cmds.rename(shinTwist_l_ik_handle[1], f'effector_{l}_shinTwist')
                cmds.parent(f'ikHandle_{l}_shinTwist', f'grp_{l}_leg')
                cmds.setAttr(f'ikHandle_{l}_shinTwist.v', False)
                # 创建约束
                self.parentCon('output_c_cog', f'jnt_{l}_thighTwist', offset=True, skipRotate=True)
                self.parentCon(f'calf_{l}', f'ikHandle_{l}_thighTwist', offset=True, skipRotate=True)
                self.parentCon('output_c_cog', f'ikHandle_{l}_thighTwist', offset=True, skipTranslate=True, name=f'ikHandle_{l}_thighTwist_parentConstraint_01')
                self.parentCon(f'foot_{l}', f'ikHandle_{l}_shinTwist', offset=True)
                if thighValue !=0:
                    self.between_joints(f'thigh_{l}',f'calf_{l}','thigh',f'thigh_{l}',thighValue)
                    for thigh in range(thighValue+1)[1:]:
                        weight_a = cmds.getAttr(f'thigh_twist_{str(thigh).zfill(2)}_{l}.translateX') / cmds.getAttr(f'calf_{l}.translateX')
                        weight_b = 1 - weight_a

                        thigh_orientCon = self.orientCon([f'thigh_{l}', f'jnt_{l}_thighTwist'], f'thigh_twist_{str(thigh).zfill(2)}_{l}')
                        cmds.setAttr(f'{thigh_orientCon}.thigh_{l}W0', weight_a)
                        cmds.setAttr(f'{thigh_orientCon}.jnt_{l}_thighTwistW1', weight_b)

                        thigh_pointCon = self.pointCon([f'thigh_{l}', f'calf_{l}'], f'thigh_twist_{str(thigh).zfill(2)}_{l}')
                        cmds.setAttr(f'{thigh_pointCon}.thigh_{l}W0', weight_b)
                        cmds.setAttr(f'{thigh_pointCon}.calf_{l}W1', weight_a)
                if shinValue !=0:
                    self.between_joints(f'foot_{l}',f'calf_{l}','calf',f'calf_{l}',shinValue)
                    for shin in range(shinValue + 1)[1:]:
                        weight_a = cmds.getAttr(f'calf_twist_{str(shin).zfill(2)}_{l}.translateX') / cmds.getAttr(f'foot_{l}.translateX')
                        weight_b = 1 - weight_a

                        shin_orientCon = self.orientCon([f'calf_{l}', f'jnt_{l}_shinTwist'], f'calf_twist_{str(shin).zfill(2)}_{l}')
                        cmds.setAttr(f'{shin_orientCon}.calf_{l}W0', weight_b)
                        cmds.setAttr(f'{shin_orientCon}.jnt_{l}_shinTwistW1', weight_a)

                        shin_pointCon = self.pointCon([f'calf_{l}', f'foot_{l}'], f'calf_twist_{str(shin).zfill(2)}_{l}')
                        cmds.setAttr(f'{shin_pointCon}.calf_{l}W0', weight_b)
                        cmds.setAttr(f'{shin_pointCon}.foot_{l}W1', weight_a)
    '''
    镜像骨骼
    '''
    def mirror_joints(self,joint_list,side):
        for l, r in zip(side[::2], side[1::2]):
            for joint in joint_list:
                # 假设镜像骨骼的命名约定为将 '_l' 改为 '_r'
                if f'_{l}' in joint:
                    mirror_joint_name = joint.replace(f'_{l}', f'_{r}')
                else:
                    continue  # 如果不是左侧骨骼，跳过

                # 检查镜像骨骼是否存在
                if cmds.objExists(mirror_joint_name):
                    # 获取原骨骼的变换信息
                    translate = cmds.xform(joint, q=True, ws=True, t=True)
                    rotate = cmds.xform(joint, q=True, ws=True, ro=True)

                    # 更新镜像骨骼的变换
                    cmds.xform(mirror_joint_name, ws=True, t=[-translate[0], translate[1], translate[2]])  # 对X轴进行镜像
                    cmds.xform(mirror_joint_name, ws=True, ro=[rotate[0], -rotate[1], -rotate[2]])  # 对旋转进行镜像处理
                    self.freeze_transform(mirror_joint_name)
                else:
                    parent=cmds.listRelatives(joint,parent=True)[0]
                    cmds.parent(joint,world=True)
                    cmds.mirrorJoint(joint, mirrorYZ=True, mirrorBehavior=True, searchReplace=(f'_{l}', f'_{r}'))
                    self.safe_parent(joint,parent)
                    if f'_{l}' in parent:
                        mirror_parent = parent.replace(f'_{l}', f'_{r}')
                        self.safe_parent(mirror_joint_name,mirror_parent)
                    else:
                        self.safe_parent(mirror_joint_name,parent)
    '''
    average_joint
    '''
    def avg_joint(self,drivers,parent='',weight=0.5):
        if parent=='':
            parent=drivers[0]
        parts = parent.split('_')
        name=f'{parts[0]}_correctiveRoot_{parts[1]}'
        if not cmds.objExists(name):
            self.create_joint(name,parent=parent)
            cmds.matchTransform(name,parent)
            self.freeze_transform(name)
        con=self.parentCon(drivers,name,offset=True,skipTranslate=True)
        cmds.setAttr(f'{con}.{drivers[0]}W0',weight)
        cmds.setAttr(f'{con}.{drivers[1]}W1', 1-weight)

    '''
    创建average_joint
    '''
    def create_average(self):
        side = self.side_list
        for l in side:
            if cmds.objExists(f'upperarm_{l}'):
                if cmds.objExists(f'jnt_{l}_upperarmTwist'):
                    self.avg_joint([f'jnt_{l}_upperarmTwist',f'clavicle_{l}'],f'upperarm_{l}')
                else:
                    self.avg_joint([f'upperarm_{l}', f'clavicle_{l}'])
                self.avg_joint([f'lowerarm_{l}',f'upperarm_{l}'])

        side = self.side_list
        for l in side:
            if cmds.objExists(f'thigh_{l}'):
                if cmds.objExists(f'jnt_{l}_thighTwist'):
                    self.avg_joint([f'jnt_{l}_thighTwist','pelvis'],f'thigh_{l}')
                else:
                    self.avg_joint([f'thigh_{l}', 'pelvis'])
                self.avg_joint([f'calf_{l}',f'thigh_{l}'])
    '''
    创建Push
    '''

    def create_push(self):

        side=self.side_list
        even_side=self.side_list[0::2]
        joint_list=[]
        for l in even_side:
            if cmds.objExists(f'clavicle_{l}'):
                joint_list.append(self.create_joint(f'clavicle_out_{l}',translate=[10.8,0,5.5],parent=f'clavicle_{l}',update=False))
                joint_list.append(self.create_joint(f'clavicle_scap_{l}',translate=[8.9,6.1,-2.4],rotate=[0,0,180],parent=f'clavicle_{l}',update=False))
            if cmds.objExists(f'upperarm_correctiveRoot_{l}'):
                joint_list.append(self.create_joint(f'upperarm_out_{l}',translate=[0,0,5.7],parent=f'upperarm_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'upperarm_in_{l}', translate=[6, 0, -4.6],rotate=[180,-48,0], parent=f'upperarm_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'upperarm_fwd_{l}', translate=[3.2, -6.5, 0],rotate=[90,0,0], parent=f'upperarm_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'upperarm_bck_{l}', translate=[0, 6.3, 0],rotate=[-90,0,0], parent=f'upperarm_correctiveRoot_{l}',update=False))
            elif cmds.objExists(f'upperarm_{l}'):
                joint_list.append(self.create_joint(f'upperarm_out_{l}', translate=[0, 0, 5.7], parent=f'upperarm_{l}'))
                joint_list.append(self.create_joint(f'upperarm_in_{l}', translate=[6, 0, -4.6], rotate=[180, -48, 0], parent=f'upperarm_{l}',update=False))
                joint_list.append(self.create_joint(f'upperarm_fwd_{l}', translate=[3.2, -6.5, 0], rotate=[90, 0, 0], parent=f'upperarm_{l}',update=False))
                joint_list.append(self.create_joint(f'upperarm_bck_{l}', translate=[0, 6.3, 0], rotate=[-90, 0, 0], parent=f'upperarm_{l}',update=False))
            if cmds.objExists(f'lowerarm_correctiveRoot_{l}'):
                joint_list.append(self.create_joint(f'lowerarm_out_{l}',translate=[0,0,2],parent=f'lowerarm_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'lowerarm_in_{l}', translate=[0, 0, -2.9],rotate=[180,0,0] ,parent=f'lowerarm_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'lowerarm_fwd_{l}', translate=[1.4, -2.7, 0],rotate=[90,0,0], parent=f'lowerarm_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'lowerarm_bck_{l}', translate=[0, 3.6, 0],rotate=[-90,0,0], parent=f'lowerarm_correctiveRoot_{l}',update=False))
            elif cmds.objExists(f'lowerarm_{l}'):
                joint_list.append(self.create_joint(f'lowerarm_out_{l}', translate=[0, 0, 2], parent=f'lowerarm_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'lowerarm_in_{l}', translate=[0, 0, -2.9], rotate=[180, 0, 0], parent=f'lowerarm_{l}',update=False))
                joint_list.append(self.create_joint(f'lowerarm_fwd_{l}', translate=[1.4, -2.7, 0], rotate=[90, 0, 0], parent=f'lowerarm_{l}',update=False))
                joint_list.append(self.create_joint(f'lowerarm_bck_{l}', translate=[0, 3.6, 0], rotate=[-90, 0, 0], parent=f'lowerarm_{l}',update=False))
            if cmds.objExists(f'hand_correctiveRoot_{l}'):
                joint_list.append(self.create_joint(f'wrist_outer_{l}', translate=[0, -1.7, 0],rotate=[90,0,0], parent=f'hand_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'wrist_inner_{l}', translate=[0, 1.7, 0], rotate=[-90, 0, 0], parent=f'hand_correctiveRoot_{l}',update=False))
            elif cmds.objExists(f'hand_{l}'):
                joint_list.append(self.create_joint(f'wrist_outer_{l}', translate=[0, -1.7, 0],rotate=[90,0,0], parent=f'hand_{l}',update=False))
                joint_list.append(self.create_joint(f'wrist_inner_{l}', translate=[0, 1.7, 0], rotate=[-90, 0, 0], parent=f'hand_{l}',update=False))
            if cmds.objExists(f'thigh_correctiveRoot_{l}'):
                joint_list.append(self.create_joint(f'thigh_out_{l}', translate=[5.9, 1.3, -4.9],rotate=[180,0,0], parent=f'thigh_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'thigh_in_{l}', translate=[-10.3, 1.3, 9.2], rotate=[0, 0, 0], parent=f'thigh_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'thigh_fwd_{l}', translate=[6.3, -7.7, 0], rotate=[90, 0, 0], parent=f'thigh_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'thigh_fwd_lwr_{l}', translate=[0, -7.9, 0], rotate=[90, 0, 0], parent=f'thigh_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'thigh_bck_{l}', translate=[3.8, 11.2, 0], rotate=[-90, 0, 0], parent=f'thigh_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'thigh_bck_lwr_{l}', translate=[-6, 10.7, 0], rotate=[-90, 0, 0], parent=f'thigh_correctiveRoot_{l}',update=False))
            elif cmds.objExists(f'thigh_{l}'):
                joint_list.append(self.create_joint(f'thigh_out_{l}', translate=[5.9, 1.3, 0],rotate=[180,0,0], parent=f'thigh_{l}',update=False))
                joint_list.append(self.create_joint(f'thigh_in_{l}', translate=[-10.3, 1.3, 9.2], rotate=[0, 0, 0], parent=f'thigh_{l}',update=False))
                joint_list.append(self.create_joint(f'thigh_fwd_{l}', translate=[6.3, -7.7, -4.9], rotate=[90, 0, 0], parent=f'thigh_{l}',update=False))
                joint_list.append(self.create_joint(f'thigh_fwd_lwr_{l}', translate=[0, -7.9, 0], rotate=[90, 0, 0], parent=f'thigh_{l}',update=False))
                joint_list.append(self.create_joint(f'thigh_bck_{l}', translate=[3.8, 11.2, 0], rotate=[-90, 0, 0], parent=f'thigh_{l}',update=False))
                joint_list.append(self.create_joint(f'thigh_bck_lwr_{l}', translate=[-6, 10.7, 0], rotate=[-90, 0, 0], parent=f'thigh_{l}',update=False))
            if cmds.objExists(f'calf_correctiveRoot_{l}'):
                joint_list.append(self.create_joint(f'calf_knee_{l}', translate=[0, -4.6, 0], rotate=[90, 0, 0], parent=f'calf_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'calf_kneeBack_{l}', translate=[0, 5.2, 0], rotate=[-90, 0, 0], parent=f'calf_correctiveRoot_{l}',update=False))
            elif cmds.objExists(f'calf_{l}'):
                joint_list.append(self.create_joint(f'calf_knee_{l}', translate=[0, -4.6, 0], rotate=[90, 0, 0], parent=f'calf_{l}',update=False))
                joint_list.append(self.create_joint(f'calf_kneeBack_{l}', translate=[0, 5.2, 0], rotate=[-90, 0, 0], parent=f'calf_{l}',update=False))
            if cmds.objExists(f'foot_correctiveRoot_{l}'):
                joint_list.append(self.create_joint(f'ankle_fwd_{l}', translate=[0, -4, 0], rotate=[90, 0, 0], parent=f'foot_correctiveRoot_{l}',update=False))
                joint_list.append(self.create_joint(f'ankle_bck_{l}', translate=[0, 3.4, 0], rotate=[-90, 0, 0], parent=f'foot_correctiveRoot_{l}',update=False))
            elif cmds.objExists(f'foot_{l}'):
                joint_list.append(self.create_joint(f'ankle_fwd_{l}', translate=[0, -4, 0], rotate=[90, 0, 0], parent=f'foot_{l}',update=False))
                joint_list.append(self.create_joint(f'ankle_bck_{l}', translate=[0, 3.4, 0], rotate=[-90, 0, 0], parent=f'foot_{l}',update=False))

            self.mirror_joints(joint_list,side=side)

    '''
    添加拉伸
    '''
    def create_stretch(self):
        if cmds.objExists('crv_c_spine'):
            cmds.addAttr('ctrl_c_spineIk',attributeType='float',defaultValue=0,longName='stretch',maxValue=1,minValue=0,niceName='开启拉伸',keyable=True)
            #创建curveInfo，并输入曲线
            self.safe_createNode('curveInfo',name='curveInfo_c_spine')
            cmds.connectAttr('crv_c_spineShape.worldSpace[0]','curveInfo_c_spine.inputCurve')
            spine_crv_length=cmds.getAttr('curveInfo_c_spine.arcLength')
            #创建add，计算增量
            self.safe_createNode('addDoubleLinear',name='add_c_spine')
            cmds.connectAttr('curveInfo_c_spine.arcLength','add_c_spine.input1')
            #创建mult，消除整体缩放带来的增量
            self.safe_createNode('multDoubleLinear',name='mult_c_spine_00')
            cmds.setAttr('mult_c_spine_00.input1',-1*spine_crv_length)
            cmds.connectAttr('ctrl_c_root.rigScale', 'mult_c_spine_00.input2')
            cmds.connectAttr('mult_c_spine_00.output','add_c_spine.input2')
            #将增量连接到骨骼
            last_spine=cmds.listRelatives('neck_01',parent=True)[0]
            parts=last_spine.split('_')
            num=1/int(parts[1])
            self.safe_createNode('multDoubleLinear',name='mult_c_spine_01')
            cmds.connectAttr('add_c_spine.output','mult_c_spine_01.input1')
            cmds.setAttr('mult_c_spine_01.input2',num)
            sa=self.get_max_translate('spine_01')
            for s in range(int(parts[1])+1)[2:]:
                add=f'add_c_spine_{str(s).zfill(2)}'
                joint_spine=f'jnt_c_spine{chr(64+s)}'
                blend = f'blend_c_spine{chr(64+s)}'
                self.safe_createNode('addDoubleLinear',name=add)
                self.safe_createNode('blendColors',name=blend)
                cmds.connectAttr('mult_c_spine_01.output',f'{add}.input1')
                original=cmds.getAttr(f'{joint_spine}.t{sa}')
                cmds.setAttr(f'{add}.input2',original)
                cmds.connectAttr(f'{add}.output',f'{blend}.color1R')
                cmds.setAttr(f'{blend}.color2R',original)
                cmds.connectAttr('ctrl_c_spineIk.stretch',f'{blend}.blender')
                cmds.connectAttr(f'{blend}.outputR',f'{joint_spine}.t{sa}')
            #连接last_spine父子约束的位置
            cmds.connectAttr(f'{last_spine}_parentConstraint_00.constraintTranslateX',f'{last_spine}.tx')
            cmds.connectAttr(f'{last_spine}_parentConstraint_00.constraintTranslateY', f'{last_spine}.ty')
            cmds.connectAttr(f'{last_spine}_parentConstraint_00.constraintTranslateZ', f'{last_spine}.tz')
            #计算样条线IK偏移
            self.safe_createNode('multiplyDivide',name='multply_c_spine')
            cmds.connectAttr('curveInfo_c_spine.arcLength','multply_c_spine.input2X')
            cmds.setAttr('multply_c_spine.input1X',spine_crv_length)
            cmds.setAttr('multply_c_spine.operation',2)

            self.safe_createNode('multDoubleLinear',name='mult_c_spine_02')
            cmds.connectAttr('multply_c_spine.outputX','mult_c_spine_02.input1')
            cmds.connectAttr('add_c_spine.output','mult_c_spine_02.input2')

            self.safe_createNode('multDoubleLinear', name='mult_c_spine_03')
            cmds.connectAttr('mult_c_spine_02.output','mult_c_spine_03.input1')
            cmds.setAttr('mult_c_spine_03.input2',0.01)
            cmds.connectAttr('mult_c_spine_03.output','ikHandle_spine.offset')

        #手臂拉伸
        side = self.side_list
        for l in side:
            if cmds.objExists(f'upperarm_{l}'):
                #判断side
                lowerarm_l_tx = cmds.getAttr(f'lowerarm_{l}.translateX')
                hand_l_tx = cmds.getAttr(f'hand_{l}.translateX')
                if l=='l':
                    color=6
                    add_l_armStretch_input2 = (lowerarm_l_tx + hand_l_tx) * -1
                elif l=='r':
                    color=13
                    add_l_armStretch_input2 = (lowerarm_l_tx + hand_l_tx)

                # 创建驱动骨骼
                self.create_joint(name=f'drv_{l}_upperarmIk', parent=f'grp_{l}_armIk')
                self.create_joint(name=f'drv_{l}_forearmIk', parent=f'drv_{l}_upperarmIk')
                self.create_joint(name=f'drv_{l}_handIk', parent=f'drv_{l}_forearmIk')
        
                cmds.matchTransform(f'drv_{l}_upperarmIk', f'upperarm_{l}')
                cmds.matchTransform(f'drv_{l}_forearmIk', f'lowerarm_{l}')
                cmds.matchTransform(f'drv_{l}_handIk', f'hand_{l}')
        
                self.freeze_transform([f'drv_{l}_upperarmIk', f'drv_{l}_forearmIk', f'drv_{l}_handIk'])
        
                # 创建ik拉伸控制器

                self.safe_createNode('transform', name=f'zero_{l}_upperarmIk')
                self.safe_parent(f'zero_{l}_upperarmIk', f'grp_{l}_armIk')
                self.safe_createNode('transform', name=f'driven_{l}_upperarmIk')
                self.safe_parent(f'driven_{l}_upperarmIk', f'zero_{l}_upperarmIk')
                self.create_joint(name=f'ctrl_{l}_upperarmIk', parent=f'driven_{l}_upperarmIk')
                cmds.matchTransform(f'zero_{l}_upperarmIk', f'upperarm_{l}')
                self.setAttrAdv(f'ctrl_{l}_upperarmIk',['jointOrientX','jointOrientY','jointOrientZ'], 0)
                self.setAttrAdv(f'ctrl_{l}_upperarmIk',['rx','ry','rz','sx','sy','sz'],channelBox=False,lock=True)
                cmds.setAttr(f'ctrl_{l}_upperarmIk.v',keyable=False)
                cmds.setAttr(f'ctrl_{l}_upperarmIk.radius',5)
                cmds.setAttr(f'ctrl_{l}_upperarmIk.overrideEnabled', True)
                cmds.setAttr(f'ctrl_{l}_upperarmIk.overrideColor', color)

                self.safe_createNode('transform', name=f'zero_{l}_forearmIk')
                self.safe_parent(f'zero_{l}_forearmIk', f'grp_{l}_armIk')
                self.safe_createNode('transform', name=f'driven_{l}_forearmIk')
                self.safe_parent(f'driven_{l}_forearmIk', f'zero_{l}_forearmIk')
                self.create_joint(name=f'ctrl_{l}_forearmIk', parent=f'driven_{l}_forearmIk')
                cmds.matchTransform(f'zero_{l}_forearmIk', f'lowerarm_{l}')
                self.setAttrAdv(f'ctrl_{l}_forearmIk', ['jointOrientX', 'jointOrientY', 'jointOrientZ'], 0)
                self.setAttrAdv(f'ctrl_{l}_forearmIk', ['rx', 'ry', 'rz', 'sx', 'sy', 'sz'], channelBox=False, lock=True)
                cmds.setAttr(f'ctrl_{l}_forearmIk.v', keyable=False)
                cmds.setAttr(f'ctrl_{l}_forearmIk.radius', 5)
                cmds.setAttr(f'ctrl_{l}_forearmIk.overrideEnabled', True)
                cmds.setAttr(f'ctrl_{l}_forearmIk.overrideColor', color)
                if not cmds.attributeQuery('stretch', node=f'ctrl_{l}_handIk', exists=True):
                    cmds.addAttr(f'ctrl_{l}_handIk', attributeType='float', defaultValue=1, maxValue=1, minValue=0, longName='stretch', niceName='开启拉伸', keyable=True)
                if not cmds.attributeQuery('subCtrlVis', node=f'ctrl_{l}_handIk', exists=True):
                    cmds.addAttr(f'ctrl_{l}_handIk', attributeType='bool',  longName='subCtrlVis', niceName='次级控制器显示', keyable=False)
                    cmds.setAttr(f'ctrl_{l}_handIk.subCtrlVis', keyable=False, channelBox=True)
                cmds.connectAttr(f'ctrl_{l}_handIk.subCtrlVis',f'zero_{l}_upperarmIk.v',f=True)
                cmds.connectAttr(f'ctrl_{l}_handIk.subCtrlVis', f'zero_{l}_forearmIk.v', f=True)
                # 设置IK
                ikHandle_l_handDriver = cmds.ikHandle(
                    startJoint=f'drv_{l}_upperarmIk',
                    endEffector=f'drv_{l}_handIk',
                    name=f'ikHandle_{l}_handDriver'
                )
                cmds.rename(ikHandle_l_handDriver[1], f'effector_{l}_handDriver')
                cmds.parent(f'ikHandle_{l}_handDriver', f'ctrl_{l}_handIk')
                cmds.setAttr(f'ikHandle_{l}_handDriver.v', False)
                cmds.setAttr(f'drv_{l}_upperarmIk.v', False)
                cmds.poleVectorConstraint(f'ctrl_{l}_armPv', f'ikHandle_{l}_handDriver')

                self.safe_delete(f'ikHandle_{l}_hand')
        
                ikHandle_l_forearm = cmds.ikHandle(
                    startJoint=f'jnt_{l}_upperarmIk',
                    endEffector=f'jnt_{l}_forearmIk',
                    solver='ikSCsolver',
                    name=f'ikHandle_{l}_forearm'
                )
                cmds.rename(ikHandle_l_forearm[1], f'effector_{l}_forearm')
                cmds.parent(f'ikHandle_{l}_forearm', f'ctrl_{l}_forearmIk')
                cmds.setAttr(f'ikHandle_{l}_forearm.v', False)
        
                ikHandle_l_hand = cmds.ikHandle(
                    startJoint=f'jnt_{l}_forearmIk',
                    endEffector=f'jnt_{l}_handIk',
                    solver='ikSCsolver',
                    name=f'ikHandle_{l}_hand'
                )
                cmds.rename(ikHandle_l_hand[1], f'effector_{l}_hand')
                cmds.parent(f'ikHandle_{l}_hand', f'drv_{l}_handIk')
                cmds.setAttr(f'ikHandle_{l}_hand.v', False)
        
                # 创建约束
                self.parentCon(f'ctrl_{l}_shoulder', f'driven_{l}_upperarmIk', offset=True)
                self.parentCon(f'drv_{l}_forearmIk', f'driven_{l}_forearmIk', offset=True)
                self.deleteCon(f'jnt_{l}_upperarmIk')
                self.parentCon(f'ctrl_{l}_upperarmIk', f'jnt_{l}_upperarmIk', skipRotate=True)
                self.parentCon(f'ctrl_{l}_upperarmIk', f'drv_{l}_upperarmIk', skipRotate=True)
                self.orientCon(f'ctrl_{l}_handIk', f'jnt_{l}_handIk')
        
                self.deleteCon(f'upperarm_{l}')
                upperarm_l_parentConstraint = self.parentCon([f'jnt_{l}_upperarmIk', f'output_{l}_upperarmFk'], f'upperarm_{l}')
                cmds.connectAttr(f'rem_{l}_armBlendIkFk.outValue', upperarm_l_parentConstraint + f'.jnt_{l}_upperarmIkW0')
                cmds.connectAttr(f'rev_{l}_armBlendIkFk.outputX', upperarm_l_parentConstraint + f'.output_{l}_upperarmFkW1')
        
                self.deleteCon(f'lowerarm_{l}')
                lowerarm_l_parentConstraint = self.parentCon([f'jnt_{l}_forearmIk', f'ctrl_{l}_forearmFk'], f'lowerarm_{l}')
                cmds.connectAttr(f'rem_{l}_armBlendIkFk.outValue', lowerarm_l_parentConstraint+ f'.jnt_{l}_forearmIkW0')
                cmds.connectAttr(f'rev_{l}_armBlendIkFk.outputX', lowerarm_l_parentConstraint + f'.ctrl_{l}_forearmFkW1')
        
                self.deleteCon(f'hand_{l}')
                hand_l_parentConstraint = self.parentCon([f'jnt_{l}_handIk', f'ctrl_{l}_handFk'], f'hand_{l}')
                cmds.connectAttr(f'rem_{l}_armBlendIkFk.outValue', hand_l_parentConstraint+ f'.jnt_{l}_handIkW0',f=True)
                cmds.connectAttr(f'rev_{l}_armBlendIkFk.outputX', hand_l_parentConstraint + f'.ctrl_{l}_handFkW1',f=True)
        
                # 创建拉伸计算
                cmds.createNode('decomposeMatrix', name=f'dm_ctrl_{l}_handIk')
                cmds.connectAttr(f'ctrl_{l}_handIk.worldMatrix[0]', f'dm_ctrl_{l}_handIk.inputMatrix', f=True)
                cmds.createNode('decomposeMatrix', name=f'dm_ctrl_{l}_upperarmIk')
                cmds.connectAttr(f'ctrl_{l}_upperarmIk.worldMatrix[0]', f'dm_ctrl_{l}_upperarmIk.inputMatrix', f=True)
                cmds.createNode('distanceBetween', name=f'dis_{l}_armStretch')
                cmds.connectAttr(f'dm_ctrl_{l}_upperarmIk.outputTranslate', f'dis_{l}_armStretch.point1', f=True)
                cmds.connectAttr(f'dm_ctrl_{l}_handIk.outputTranslate', f'dis_{l}_armStretch.point2', f=True)
                cmds.createNode('addDoubleLinear', name=f'add_{l}_armStretch')
                cmds.connectAttr(f'dis_{l}_armStretch.distance', f'add_{l}_armStretch.input1', f=True)

                cmds.setAttr(f'add_{l}_armStretch.input2', add_l_armStretch_input2)
        
                cmds.createNode('multDoubleLinear', name=f'mult_{l}_forearmStretch')
                cmds.connectAttr(f'add_{l}_armStretch.output', f'mult_{l}_forearmStretch.input1', f=True)
                mult_l_forearmStretch_input2 = lowerarm_l_tx / add_l_armStretch_input2*-1
                cmds.setAttr(f'mult_{l}_forearmStretch.input2', mult_l_forearmStretch_input2)
        
                cmds.createNode('multDoubleLinear', name=f'mult_{l}_handStretch')
                cmds.connectAttr(f'add_{l}_armStretch.output', f'mult_{l}_handStretch.input1', f=True)
                mult_l_handStretch_input2 = hand_l_tx / add_l_armStretch_input2*-1
                cmds.setAttr(f'mult_{l}_handStretch.input2', mult_l_handStretch_input2)
        
                cmds.createNode('addDoubleLinear', name=f'add_{l}_forearmStretch')
                cmds.connectAttr(f'mult_{l}_forearmStretch.output', f'add_{l}_forearmStretch.input1', f=True)
                cmds.setAttr(f'add_{l}_forearmStretch.input2', lowerarm_l_tx)
        
                cmds.createNode('addDoubleLinear', name=f'add_{l}_handStretch')
                cmds.connectAttr(f'mult_{l}_handStretch.output', f'add_{l}_handStretch.input1', f=True)
                cmds.setAttr(f'add_{l}_handStretch.input2', hand_l_tx)
        
                cmds.createNode('condition', name=f'cond_{l}_armStretch')
                cmds.connectAttr(f'add_{l}_armStretch.output', f'cond_{l}_armStretch.firstTerm', f=True)
                cmds.setAttr(f'cond_{l}_armStretch.operation', 2)
                cmds.connectAttr(f'add_{l}_forearmStretch.output', f'cond_{l}_armStretch.colorIfTrueR', f=True)
                cmds.connectAttr(f'add_{l}_handStretch.output', f'cond_{l}_armStretch.colorIfTrueG', f=True)
                cmds.setAttr(f'cond_{l}_armStretch.colorIfFalseR', lowerarm_l_tx)
                cmds.setAttr(f'cond_{l}_armStretch.colorIfFalseG', hand_l_tx)
        
                cmds.createNode('blendColors', name=f'blend_{l}_armStretch')
                cmds.connectAttr(f'ctrl_{l}_handIk.stretch', f'blend_{l}_armStretch.blender', f=True)
                cmds.connectAttr(f'cond_{l}_armStretch.outColor', f'blend_{l}_armStretch.color1', f=True)
                cmds.setAttr(f'blend_{l}_armStretch.color2R', lowerarm_l_tx)
                cmds.setAttr(f'blend_{l}_armStretch.color2G', hand_l_tx)
        
                cmds.connectAttr(f'blend_{l}_armStretch.outputR', f'drv_{l}_forearmIk.translateX', f=True)
                cmds.connectAttr(f'blend_{l}_armStretch.outputG', f'drv_{l}_handIk.translateX', f=True)
        
                cmds.createNode('decomposeMatrix', name=f'dm_ctrl_{l}_forearmIk')
                cmds.connectAttr(f'ctrl_{l}_forearmIk.worldMatrix[0]', f'dm_ctrl_{l}_forearmIk.inputMatrix', f=True)
                cmds.createNode('distanceBetween', name=f'dis_{l}_forearmStretch')
                cmds.connectAttr(f'dm_ctrl_{l}_upperarmIk.outputTranslate', f'dis_{l}_forearmStretch.point1', f=True)
                cmds.connectAttr(f'dm_ctrl_{l}_forearmIk.outputTranslate', f'dis_{l}_forearmStretch.point2', f=True)
                if l=='l':
                    cmds.connectAttr(f'dis_{l}_forearmStretch.distance', f'jnt_{l}_forearmIk.translateX', f=True)
                elif l=='r':
                    self.safe_createNode('multDoubleLinear',name=f'mult_{l}_forearmIk')
                    cmds.connectAttr(f'dis_{l}_forearmStretch.distance',f'mult_{l}_forearmIk.input1', f=True)
                    cmds.setAttr(f'mult_{l}_forearmIk.input2',-1)
                    cmds.connectAttr(f'mult_{l}_forearmIk.output',f'jnt_{l}_forearmIk.translateX', f=True)
        
                cmds.createNode('decomposeMatrix', name=f'dm_drv_{l}_handIk')
                cmds.connectAttr(f'drv_{l}_handIk.worldMatrix[0]', f'dm_drv_{l}_handIk.inputMatrix', f=True)
                cmds.createNode('distanceBetween', name=f'dis_{l}_handStretch')
                cmds.connectAttr(f'dm_ctrl_{l}_forearmIk.outputTranslate', f'dis_{l}_handStretch.point1', f=True)
                cmds.connectAttr(f'dm_drv_{l}_handIk.outputTranslate', f'dis_{l}_handStretch.point2', f=True)
                if l=='l':
                    cmds.connectAttr(f'dis_{l}_handStretch.distance', f'jnt_{l}_handIk.translateX', f=True)
                elif l=='r':
                    self.safe_createNode('multDoubleLinear',name=f'mult_{l}_handIk')
                    cmds.connectAttr(f'dis_{l}_handStretch.distance',f'mult_{l}_handIk.input1', f=True)
                    cmds.setAttr(f'mult_{l}_handIk.input2',-1)
                    cmds.connectAttr(f'mult_{l}_handIk.output',f'jnt_{l}_handIk.translateX', f=True)
        # 腿部拉伸
        side = self.side_list
        for l in side:
            if cmds.objExists(f'thigh_{l}'):

                # 创建驱动骨骼
                self.create_joint(name=f'drv_{l}_thighIk', parent=f'grp_{l}_legIk')
                self.create_joint(name=f'drv_{l}_shinIk', parent=f'drv_{l}_thighIk')
                self.create_joint(name=f'drv_{l}_footIk', parent=f'drv_{l}_shinIk')

                cmds.matchTransform(f'drv_{l}_thighIk', f'thigh_{l}')
                cmds.matchTransform(f'drv_{l}_shinIk', f'calf_{l}')
                cmds.matchTransform(f'drv_{l}_footIk', f'foot_{l}')

                self.freeze_transform(name=[f'drv_{l}_thighIk', f'drv_{l}_shinIk', f'drv_{l}_footIk'])

                calf_l_tx = cmds.getAttr(f'drv_{l}_shinIk.translateX')
                foot_l_tx = cmds.getAttr(f'drv_{l}_footIk.translateX')
                # 判断side：
                if l == 'l':
                    color = 6
                    add_l_legStretch_input2 = (calf_l_tx + foot_l_tx) * -1
                    if self.get_max_translate('calf_l')=='-x':
                        add_l_legStretch_input2 = (calf_l_tx + foot_l_tx)

                elif l == 'r':
                    color = 13
                    add_l_legStretch_input2 = (calf_l_tx + foot_l_tx)
                    if self.get_max_translate('calf_l')=='-x':
                        add_l_legStretch_input2 = (calf_l_tx + foot_l_tx) * -1

                # 创建ik拉伸控制器
                self.safe_createNode('transform', name=f'zero_{l}_thighIk')
                self.safe_parent(f'zero_{l}_thighIk', f'grp_{l}_legIk')
                self.safe_createNode('transform', name=f'driven_{l}_thighIk')
                self.safe_parent(f'driven_{l}_thighIk', f'zero_{l}_thighIk')
                self.create_joint(name=f'ctrl_{l}_thighIk', parent=f'driven_{l}_thighIk')
                cmds.matchTransform(f'zero_{l}_thighIk', f'thigh_{l}')
                self.setAttrAdv(f'ctrl_{l}_thighIk', ['jointOrientX', 'jointOrientY', 'jointOrientZ'], 0)
                self.setAttrAdv(f'ctrl_{l}_thighIk', ['rx', 'ry', 'rz', 'sx', 'sy', 'sz'], channelBox=False, lock=True)
                cmds.setAttr(f'ctrl_{l}_thighIk.v', keyable=False)
                cmds.setAttr(f'ctrl_{l}_thighIk.radius', 5)
                cmds.setAttr(f'ctrl_{l}_thighIk.overrideEnabled', True)
                cmds.setAttr(f'ctrl_{l}_thighIk.overrideColor', color)

                self.safe_createNode('transform', name=f'zero_{l}_shinIk')
                self.safe_parent(f'zero_{l}_shinIk', f'grp_{l}_legIk')
                self.safe_createNode('transform', name=f'driven_{l}_shinIk')
                self.safe_parent(f'driven_{l}_shinIk', f'zero_{l}_shinIk')
                self.create_joint(name=f'ctrl_{l}_shinIk', parent=f'driven_{l}_shinIk')
                cmds.matchTransform(f'zero_{l}_shinIk', f'calf_{l}')
                self.setAttrAdv(f'ctrl_{l}_shinIk', ['jointOrientX', 'jointOrientY', 'jointOrientZ'], 0)
                self.setAttrAdv(f'ctrl_{l}_shinIk', ['rx', 'ry', 'rz', 'sx', 'sy', 'sz'], channelBox=False, lock=True)
                cmds.setAttr(f'ctrl_{l}_shinIk.v', keyable=False)
                cmds.setAttr(f'ctrl_{l}_shinIk.radius', 5)
                cmds.setAttr(f'ctrl_{l}_shinIk.overrideEnabled', True)
                cmds.setAttr(f'ctrl_{l}_shinIk.overrideColor', color)

                if not cmds.attributeQuery('stretch', node=f'ctrl_{l}_footIk', exists=True):
                    cmds.addAttr(f'ctrl_{l}_footIk', attributeType='float', defaultValue=1, maxValue=1, minValue=0, longName='stretch', niceName='开启拉伸', keyable=True)
                if not cmds.attributeQuery('subCtrlVis', node=f'ctrl_{l}_footIk', exists=True):
                    cmds.addAttr(f'ctrl_{l}_footIk', attributeType='bool', longName='subCtrlVis', niceName='次级控制器显示')
                    cmds.setAttr(f'ctrl_{l}_footIk.subCtrlVis',channelBox=True,keyable=False)
                cmds.connectAttr(f'ctrl_{l}_footIk.subCtrlVis', f'zero_{l}_thighIk.v', f=True)
                cmds.connectAttr(f'ctrl_{l}_footIk.subCtrlVis', f'zero_{l}_shinIk.v', f=True)

                # 设置IK
                ikHandle_l_footDriver = cmds.ikHandle(
                    startJoint=f'drv_{l}_thighIk',
                    endEffector=f'drv_{l}_footIk',
                    name=f'ikHandle_{l}_footDriver'
                )
                cmds.rename(ikHandle_l_footDriver[1], f'effector_{l}_footDriver')
                cmds.parent(f'ikHandle_{l}_footDriver', f'jnt_{l}_ballFoot')
                cmds.setAttr(f'ikHandle_{l}_footDriver.v', False)
                cmds.setAttr(f'drv_{l}_thighIk.v', False)
                cmds.poleVectorConstraint(f'ctrl_{l}_legPv', f'ikHandle_{l}_footDriver')
                self.safe_delete(f'ikHandle_{l}_foot')

                ikHandle_l_shin = cmds.ikHandle(
                    startJoint=f'jnt_{l}_thighIk',
                    endEffector=f'jnt_{l}_shinIk',
                    solver='ikSCsolver',
                    name=f'ikHandle_{l}_shin'
                )
                cmds.rename(ikHandle_l_shin[1], f'effector_{l}_shin')
                cmds.parent(f'ikHandle_{l}_shin', f'ctrl_{l}_shinIk')
                cmds.setAttr(f'ikHandle_{l}_shin.v', False)

                ikHandle_l_foot = cmds.ikHandle(
                    startJoint=f'jnt_{l}_shinIk',
                    endEffector=f'jnt_{l}_footIk',
                    solver='ikSCsolver',
                    name=f'ikHandle_{l}_foot'
                )
                cmds.rename(ikHandle_l_foot[1], f'effector_{l}_foot')
                cmds.parent(f'ikHandle_{l}_foot', f'drv_{l}_footIk')
                cmds.setAttr(f'ikHandle_{l}_foot.v', False)

                # 创建约束
                self.parentCon('output_c_cog', f'driven_{l}_thighIk', offset=True)
                self.parentCon(f'drv_{l}_shinIk', f'driven_{l}_shinIk', offset=True)
                self.deleteCon(f'jnt_{l}_thighIk')
                self.parentCon(f'ctrl_{l}_thighIk', f'jnt_{l}_thighIk', skipRotate=True)
                self.parentCon(f'ctrl_{l}_thighIk', f'drv_{l}_thighIk', skipRotate=True)
                self.orientCon(f'ctrl_{l}_footIk', f'jnt_{l}_footIk')

                self.deleteCon(f'thigh_{l}')
                thigh_l_parentConstraint = self.parentCon([f'jnt_{l}_thighIk', f'ctrl_{l}_thighFk'], f'thigh_{l}')
                cmds.connectAttr(f'rem_{l}_legBlendIkFk.outValue', thigh_l_parentConstraint + f'.jnt_{l}_thighIkW0')
                cmds.connectAttr(f'rev_{l}_legBlendIkFk.outputX', thigh_l_parentConstraint + f'.ctrl_{l}_thighFkW1')

                self.deleteCon(f'calf_{l}')
                calf_l_parentConstraint = self.parentCon([f'jnt_{l}_shinIk', f'ctrl_{l}_shinFk'], f'calf_{l}')
                cmds.connectAttr(f'rem_{l}_legBlendIkFk.outValue', calf_l_parentConstraint + f'.jnt_{l}_shinIkW0')
                cmds.connectAttr(f'rev_{l}_legBlendIkFk.outputX', calf_l_parentConstraint + f'.ctrl_{l}_shinFkW1')

                self.deleteCon(f'foot_{l}')
                foot_l_parentConstraint = self.parentCon([f'jnt_{l}_footIk', f'ctrl_{l}_footFk'], f'foot_{l}')
                cmds.connectAttr(f'rem_{l}_legBlendIkFk.outValue', foot_l_parentConstraint + f'.jnt_{l}_footIkW0')
                cmds.connectAttr(f'rev_{l}_legBlendIkFk.outputX', foot_l_parentConstraint + f'.ctrl_{l}_footFkW1')

                # 创建拉伸计算
                self.safe_createNode('decomposeMatrix', name=f'dm_jnt_{l}_ballFoot')
                cmds.connectAttr(f'jnt_{l}_ballFoot.worldMatrix[0]', f'dm_jnt_{l}_ballFoot.inputMatrix', f=True)
                self.safe_createNode('decomposeMatrix', name=f'dm_ctrl_{l}_thighIk')
                cmds.connectAttr(f'ctrl_{l}_thighIk.worldMatrix[0]', f'dm_ctrl_{l}_thighIk.inputMatrix', f=True)
                self.safe_createNode('distanceBetween', name=f'dis_{l}_legStretch')
                cmds.connectAttr(f'dm_ctrl_{l}_thighIk.outputTranslate', f'dis_{l}_legStretch.point1', f=True)
                cmds.connectAttr(f'dm_jnt_{l}_ballFoot.outputTranslate', f'dis_{l}_legStretch.point2', f=True)
                self.safe_createNode('addDoubleLinear', name=f'add_{l}_legStretch')
                cmds.connectAttr(f'dis_{l}_legStretch.distance', f'add_{l}_legStretch.input1', f=True)

                cmds.setAttr(f'add_{l}_legStretch.input2', add_l_legStretch_input2)

                self.safe_createNode('multDoubleLinear', name=f'mult_{l}_shinStretch')
                cmds.connectAttr(f'add_{l}_legStretch.output', f'mult_{l}_shinStretch.input1', f=True)
                mult_l_shinStretch_input2 = calf_l_tx / add_l_legStretch_input2 * -1
                cmds.setAttr(f'mult_{l}_shinStretch.input2', mult_l_shinStretch_input2)

                self.safe_createNode('multDoubleLinear', name=f'mult_{l}_footStretch')
                cmds.connectAttr(f'add_{l}_legStretch.output', f'mult_{l}_footStretch.input1', f=True)
                mult_l_footStretch_input2 = foot_l_tx / add_l_legStretch_input2 * -1
                cmds.setAttr(f'mult_{l}_footStretch.input2', mult_l_footStretch_input2)

                self.safe_createNode('addDoubleLinear', name=f'add_{l}_shinStretch')
                cmds.connectAttr(f'mult_{l}_shinStretch.output', f'add_{l}_shinStretch.input1', f=True)
                cmds.setAttr(f'add_{l}_shinStretch.input2', calf_l_tx)

                self.safe_createNode('addDoubleLinear', name=f'add_{l}_footStretch')
                cmds.connectAttr(f'mult_{l}_footStretch.output', f'add_{l}_footStretch.input1', f=True)
                cmds.setAttr(f'add_{l}_footStretch.input2', foot_l_tx)

                self.safe_createNode('condition', name=f'cond_{l}_legStretch')
                cmds.connectAttr(f'add_{l}_legStretch.output', f'cond_{l}_legStretch.firstTerm', f=True)
                cmds.setAttr(f'cond_{l}_legStretch.operation', 2)
                cmds.connectAttr(f'add_{l}_shinStretch.output', f'cond_{l}_legStretch.colorIfTrueR', f=True)
                cmds.connectAttr(f'add_{l}_footStretch.output', f'cond_{l}_legStretch.colorIfTrueG', f=True)
                cmds.setAttr(f'cond_{l}_legStretch.colorIfFalseR', calf_l_tx)
                cmds.setAttr(f'cond_{l}_legStretch.colorIfFalseG', foot_l_tx)

                self.safe_createNode('blendColors', name=f'blend_{l}_legStretch')
                cmds.connectAttr(f'ctrl_{l}_footIk.stretch', f'blend_{l}_legStretch.blender', f=True)
                cmds.connectAttr(f'cond_{l}_legStretch.outColor', f'blend_{l}_legStretch.color1', f=True)
                cmds.setAttr(f'blend_{l}_legStretch.color2R', calf_l_tx)
                cmds.setAttr(f'blend_{l}_legStretch.color2G', foot_l_tx)

                cmds.connectAttr(f'blend_{l}_legStretch.outputR', f'drv_{l}_shinIk.translateX', f=True)
                cmds.connectAttr(f'blend_{l}_legStretch.outputG', f'drv_{l}_footIk.translateX', f=True)

                self.safe_createNode('decomposeMatrix', name=f'dm_ctrl_{l}_shinIk')
                cmds.connectAttr(f'ctrl_{l}_shinIk.worldMatrix[0]', f'dm_ctrl_{l}_shinIk.inputMatrix', f=True)
                self.safe_createNode('distanceBetween', name=f'dis_{l}_shinStretch')
                cmds.connectAttr(f'dm_ctrl_{l}_thighIk.outputTranslate', f'dis_{l}_shinStretch.point1', f=True)
                cmds.connectAttr(f'dm_ctrl_{l}_shinIk.outputTranslate', f'dis_{l}_shinStretch.point2', f=True)
                if l=='l':
                    if self.get_max_translate('calf_l') == 'x':
                        cmds.connectAttr(f'dis_{l}_shinStretch.distance', f'jnt_{l}_shinIk.translateX', f=True)
                    else:
                        self.safe_createNode('multDoubleLinear', name=f'mult_{l}_shinIk')
                        cmds.connectAttr(f'dis_{l}_shinStretch.distance', f'mult_{l}_shinIk.input1', f=True)
                        cmds.setAttr(f'mult_{l}_shinIk.input2', -1)
                        cmds.connectAttr(f'mult_{l}_shinIk.output', f'jnt_{l}_shinIk.translateX', f=True)
                elif l=='r':
                    if self.get_max_translate('calf_l') == 'x':
                        self.safe_createNode('multDoubleLinear',name=f'mult_{l}_shinIk')
                        cmds.connectAttr(f'dis_{l}_shinStretch.distance',f'mult_{l}_shinIk.input1', f=True)
                        cmds.setAttr(f'mult_{l}_shinIk.input2',-1)
                        cmds.connectAttr(f'mult_{l}_shinIk.output',f'jnt_{l}_shinIk.translateX', f=True)
                    else:
                        cmds.connectAttr(f'dis_{l}_shinStretch.distance', f'jnt_{l}_shinIk.translateX', f=True)

                self.safe_createNode('decomposeMatrix', name=f'dm_drv_{l}_footIk')
                cmds.connectAttr(f'drv_{l}_footIk.worldMatrix[0]', f'dm_drv_{l}_footIk.inputMatrix', f=True)
                self.safe_createNode('distanceBetween', name=f'dis_{l}_footStretch')
                cmds.connectAttr(f'dm_ctrl_{l}_shinIk.outputTranslate', f'dis_{l}_footStretch.point1', f=True)
                cmds.connectAttr(f'dm_drv_{l}_footIk.outputTranslate', f'dis_{l}_footStretch.point2', f=True)
                if l=='l':
                    if self.get_max_translate('foot_l') == 'x':
                        cmds.connectAttr(f'dis_{l}_footStretch.distance', f'jnt_{l}_footIk.translateX', f=True)
                    else:
                        self.safe_createNode('multDoubleLinear', name=f'mult_{l}_footIk')
                        cmds.connectAttr(f'dis_{l}_footStretch.distance', f'mult_{l}_footIk.input1', f=True)
                        cmds.setAttr(f'mult_{l}_footIk.input2', -1)
                        cmds.connectAttr(f'mult_{l}_footIk.output', f'jnt_{l}_footIk.translateX', f=True)
                elif l=='r':
                    if self.get_max_translate('foot_l') == 'x':
                        self.safe_createNode('multDoubleLinear',name=f'mult_{l}_footIk')
                        cmds.connectAttr(f'dis_{l}_footStretch.distance',f'mult_{l}_footIk.input1', f=True)
                        cmds.setAttr(f'mult_{l}_footIk.input2',-1)
                        cmds.connectAttr(f'mult_{l}_footIk.output',f'jnt_{l}_footIk.translateX', f=True)
                    else:
                        cmds.connectAttr(f'dis_{l}_footStretch.distance', f'jnt_{l}_footIk.translateX', f=True)
    '''
    搜索和替换
    '''

    def search_replace(self):
        cmds.undoInfo(openChunk=True)
        old_part = self.le0000.text()
        new_part = self.le0001.text()

        select_objs = cmds.ls(selection=True,long=True)
        select_objs.sort(key=lambda x: x.count('|'), reverse=True)
        if old_part == '':
            cmds.warning('搜索不能为空')
        else:
            for obj in select_objs:
                short_name = obj.split('|')[-1]
                if old_part == '$':
                    new_name = short_name + new_part
                    print(new_name)
                    cmds.rename(obj,new_name)
                elif old_part == '#':
                    new_name = new_part+short_name
                    print(new_name)
                    cmds.rename(obj,new_name)
                elif '*' in old_part:
                    star_index = old_part.index('*')
                    if star_index + 1 < len(old_part):#如果*后有字符
                        number_part =old_part[star_index + 1:]
                    else:
                        number_part = old_part[:star_index]
                    print(number_part)
                    if number_part.isdigit():
                        number = int(number_part)
                        if old_part.startswith(str(number) + '*'):
                            # 替换前三位
                            if len(short_name ) >= number:
                                new_name = new_part + short_name[number:]
                                print(new_name)
                                cmds.rename(obj, new_name)
                        elif old_part.endswith('*' + str(number)):
                            # 替换后三位
                            if len(short_name ) >= number:
                                new_name = short_name [:-number] + new_part
                                print(new_name)
                                cmds.rename(obj, new_name)
                elif ':' in old_part:
                    start, end = map(int, old_part.split(':'))
                    # 减一
                    start -= 1
                    if len(obj)>=end and start>=0:
                        new_name = short_name[:start] + new_part + short_name[end:]
                        cmds.rename(obj,new_name)
                    else:
                        cmds.warning('输入大于等于1的值或超出原名称范围')
                elif old_part in obj:
                    new_name = short_name .replace(old_part, new_part)
                    print(new_name)
                    cmds.rename(obj, new_name)
            cmds.undoInfo(closeChunk=True)
    '''
    吸附
    '''
    def snap_to_pivot(self):

        # get selected nodes, the last one is the one need to be snapped, others are drivers
        selected_nodes = cmds.ls(selection=True, flatten=True)

        if not selected_nodes or len(selected_nodes) < 2:
            cmds.warning('需要选中物体数量大于2')
        else:
            driver_nodes = selected_nodes[:-1]
            driven_node = selected_nodes[-1]

            # get driver nodes' xyz in different lists
            drivers_x = []
            drivers_y = []
            drivers_z = []

            for driver in driver_nodes:
                pos = cmds.xform(driver, query=True, translation=True, worldSpace=True)
                drivers_x.append(pos[0])
                drivers_y.append(pos[1])
                drivers_z.append(pos[2])

            # get maximum and minimum values
            max_x = max(drivers_x)
            min_x = min(drivers_x)

            max_y = max(drivers_y)
            min_y = min(drivers_y)

            max_z = max(drivers_z)
            min_z = min(drivers_z)

            # get center position for xyz
            pos_x = 0.5 * max_x + 0.5 * min_x
            pos_y = 0.5 * max_y + 0.5 * min_y
            pos_z = 0.5 * max_z + 0.5 * min_z

            # set driven node's position
            cmds.xform(driven_node, translation=[pos_x, pos_y, pos_z], worldSpace=True)

    '''
    创建刀光
    '''

    def create_ghost(self):
        select_objs = cmds.ls(selection=True)
        crv_00 = select_objs[0]
        ctrl = select_objs[1]
        parts = ctrl.split('_')
        name = '_'.join(parts[1:])

        crv_01 = cmds.duplicate(crv_00)[0]
        crv_02 = cmds.duplicate(crv_01)[0]
        self.parentCon(ctrl, crv_00, offset=True)
        cmds.setAttr(f'{crv_00}.v', False)
        cmds.setAttr(f'{crv_01}.v', False)
        cmds.setAttr(f'{crv_02}.v', False)
        # 创建属性
        if not cmds.attributeQuery('ghostVis', node=ctrl, exists=True):
            cmds.addAttr(ctrl, attributeType='bool', keyable=False, longName='ghostVis', niceName='残影显示')
            cmds.setAttr(f'{ctrl}.ghostVis', channelBox=True)
        if not cmds.attributeQuery('ghostTimeOffset', node=ctrl, exists=True):
            cmds.addAttr(ctrl, attributeType='float', keyable=True, longName='ghostTimeOffset', niceName='残影时间偏移')
        if not cmds.attributeQuery('uNumber', node=ctrl, exists=True):
            cmds.addAttr(ctrl, attributeType='long', keyable=False, longName='uNumber', niceName='横向细分')
            cmds.setAttr(f'{ctrl}.uNumber', channelBox=True)
        if not cmds.attributeQuery('vNumber', node=ctrl, exists=True):
            cmds.addAttr(ctrl, attributeType='long', keyable=False, longName='vNumber', niceName='竖向细分')
            cmds.setAttr(f'{ctrl}.vNumber', channelBox=True)

        self.safe_createNode('plusMinusAverage', name=f'pma_{name}')
        self.safe_createNode('multDoubleLinear', name=f'mult_{name}_01')
        self.safe_createNode('multDoubleLinear', name=f'mult_{name}_02')
        cmds.connectAttr(f'{ctrl}.ghostTimeOffset', f'mult_{name}_01.input1')
        cmds.connectAttr(f'{ctrl}.ghostTimeOffset', f'mult_{name}_02.input1')
        cmds.setAttr(f'mult_{name}_01.input2', -0.5)
        cmds.setAttr(f'mult_{name}_02.input2', -1)

        cmds.connectAttr('time1.outTime', f'pma_{name}.input3D[0].input3Dx')
        cmds.connectAttr('time1.outTime', f'pma_{name}.input3D[0].input3Dy')

        cmds.connectAttr(f'mult_{name}_01.output', f'pma_{name}.input3D[1].input3Dx')
        cmds.connectAttr(f'mult_{name}_02.output', f'pma_{name}.input3D[1].input3Dy')
        self.safe_createNode('frameCache', name=f'fc_{name}_tx_01')
        self.safe_createNode('frameCache', name=f'fc_{name}_ty_01')
        self.safe_createNode('frameCache', name=f'fc_{name}_tz_01')
        self.safe_createNode('frameCache', name=f'fc_{name}_rx_01')
        self.safe_createNode('frameCache', name=f'fc_{name}_ry_01')
        self.safe_createNode('frameCache', name=f'fc_{name}_rz_01')
        cmds.connectAttr(f'{crv_00}.tx', f'fc_{name}_tx_01.stream')
        cmds.connectAttr(f'pma_{name}.output3Dx', f'fc_{name}_tx_01.varyTime')
        cmds.connectAttr(f'fc_{name}_tx_01.varying', f'{crv_01}.tx')

        cmds.connectAttr(f'{crv_00}.ty', f'fc_{name}_ty_01.stream')
        cmds.connectAttr(f'pma_{name}.output3Dx', f'fc_{name}_ty_01.varyTime')
        cmds.connectAttr(f'fc_{name}_ty_01.varying', f'{crv_01}.ty')

        cmds.connectAttr(f'{crv_00}.tz', f'fc_{name}_tz_01.stream')
        cmds.connectAttr(f'pma_{name}.output3Dx', f'fc_{name}_tz_01.varyTime')
        cmds.connectAttr(f'fc_{name}_tz_01.varying', f'{crv_01}.tz')

        cmds.connectAttr(f'{crv_00}.rx', f'fc_{name}_rx_01.stream')
        cmds.connectAttr(f'pma_{name}.output3Dx', f'fc_{name}_rx_01.varyTime')
        cmds.connectAttr(f'fc_{name}_rx_01.varying', f'{crv_01}.rx')

        cmds.connectAttr(f'{crv_00}.ry', f'fc_{name}_ry_01.stream')
        cmds.connectAttr(f'pma_{name}.output3Dx', f'fc_{name}_ry_01.varyTime')
        cmds.connectAttr(f'fc_{name}_ry_01.varying', f'{crv_01}.ry')

        cmds.connectAttr(f'{crv_00}.rz', f'fc_{name}_rz_01.stream')
        cmds.connectAttr(f'pma_{name}.output3Dx', f'fc_{name}_rz_01.varyTime')
        cmds.connectAttr(f'fc_{name}_rz_01.varying', f'{crv_01}.rz')

        self.safe_createNode('frameCache', name=f'fc_{name}_tx_02')
        self.safe_createNode('frameCache', name=f'fc_{name}_ty_02')
        self.safe_createNode('frameCache', name=f'fc_{name}_tz_02')
        self.safe_createNode('frameCache', name=f'fc_{name}_rx_02')
        self.safe_createNode('frameCache', name=f'fc_{name}_ry_02')
        self.safe_createNode('frameCache', name=f'fc_{name}_rz_02')
        cmds.connectAttr(f'{crv_00}.tx', f'fc_{name}_tx_02.stream')
        cmds.connectAttr(f'pma_{name}.output3Dy', f'fc_{name}_tx_02.varyTime')
        cmds.connectAttr(f'fc_{name}_tx_02.varying', f'{crv_02}.tx')

        cmds.connectAttr(f'{crv_00}.ty', f'fc_{name}_ty_02.stream')
        cmds.connectAttr(f'pma_{name}.output3Dy', f'fc_{name}_ty_02.varyTime')
        cmds.connectAttr(f'fc_{name}_ty_02.varying', f'{crv_02}.ty')

        cmds.connectAttr(f'{crv_00}.tz', f'fc_{name}_tz_02.stream')
        cmds.connectAttr(f'pma_{name}.output3Dy', f'fc_{name}_tz_02.varyTime')
        cmds.connectAttr(f'fc_{name}_tz_02.varying', f'{crv_02}.tz')

        cmds.connectAttr(f'{crv_00}.rx', f'fc_{name}_rx_02.stream')
        cmds.connectAttr(f'pma_{name}.output3Dy', f'fc_{name}_rx_02.varyTime')
        cmds.connectAttr(f'fc_{name}_rx_02.varying', f'{crv_02}.rx')

        cmds.connectAttr(f'{crv_00}.ry', f'fc_{name}_ry_02.stream')
        cmds.connectAttr(f'pma_{name}.output3Dy', f'fc_{name}_ry_02.varyTime')
        cmds.connectAttr(f'fc_{name}_ry_02.varying', f'{crv_02}.ry')

        cmds.connectAttr(f'{crv_00}.rz', f'fc_{name}_rz_02.stream')
        cmds.connectAttr(f'pma_{name}.output3Dy', f'fc_{name}_rz_02.varyTime')
        cmds.connectAttr(f'fc_{name}_rz_02.varying', f'{crv_02}.rz')

        cmds.xform(crv_01, scale=[1.005, 1.005, 1.005])
        cmds.xform(crv_02, scale=[1.01, 1.01, 1.01])

        loft = cmds.loft(crv_00, crv_01, crv_02, ch=True, polygon=1, uniform=True, close=False, autoReverse=True)
        history_nodes = cmds.listHistory(loft[0])
        nt = cmds.ls(history_nodes, type='nurbsTessellate')
        cmds.rename(nt, f'nt_{name}')
        cmds.rename(loft[0], f'loft_{name}Surface')
        cmds.rename(loft[1], f'loft_{name}')
        cmds.setAttr(f'nt_{name}.polygonType', 1)
        cmds.setAttr(f'nt_{name}.format', 2)
        cmds.setAttr(f'nt_{name}.uType', 2)
        cmds.setAttr(f'nt_{name}.vType', 2)
        cmds.connectAttr(f'{ctrl}.uNumber', f'nt_{name}.uNumber')
        cmds.connectAttr(f'{ctrl}.vNumber', f'nt_{name}.vNumber')
        cmds.connectAttr(f'{ctrl}.ghostVis', f'loft_{name}Surface.v')

    '''
    万向驱动
    '''
    def universal_drive(self):
        # 获取选中对象
        objs = cmds.ls(selection=True)
        obj = objs[0]
        # 开始记录撤销信息
        cmds.undoInfo(openChunk=True)
        # 添加属性
        cmds.addAttr(obj, longName="angle", attributeType="float", defaultValue=0.0, keyable=True)
        cmds.addAttr(obj, longName="direction", attributeType="float", defaultValue=0.0, keyable=True)
        cmds.addAttr(obj, longName="rotate180", attributeType="float", defaultValue=0.0, keyable=True)
        cmds.addAttr(obj, longName="direction0", attributeType="float", defaultValue=0.0, keyable=True)
        cmds.addAttr(obj, longName="direction90", attributeType="float", defaultValue=0.0, keyable=True)
        cmds.addAttr(obj, longName="direction180", attributeType="float", defaultValue=0.0, keyable=True)
        cmds.addAttr(obj, longName="direction270", attributeType="float", defaultValue=0.0, keyable=True)
        cmds.addAttr(obj, longName="drivenFwd", attributeType="float", defaultValue=0.0, keyable=True)
        cmds.addAttr(obj, longName="drivenOut", attributeType="float", defaultValue=0.0, keyable=True)
        cmds.addAttr(obj, longName="drivenBck", attributeType="float", defaultValue=0.0, keyable=True)
        cmds.addAttr(obj, longName="drivenIn", attributeType="float", defaultValue=0.0, keyable=True)

        # 创建节点
        pointMatrixMult_node = cmds.createNode('pointMatrixMult')
        angleBetween_angle_node = cmds.createNode('angleBetween')
        angleBetween_direction_node = cmds.createNode('angleBetween')
        plusMinusAverage_node = cmds.createNode('plusMinusAverage')
        condition_node = cmds.createNode('condition')
        plusMinusAverage_fwd = cmds.createNode('plusMinusAverage')
        plusMinusAverage_bck = cmds.createNode('plusMinusAverage')
        plusMinusAverage_in = cmds.createNode('plusMinusAverage')
        plusMinusAverage_out = cmds.createNode('plusMinusAverage')

        cmds.setAttr(plusMinusAverage_fwd + '.operation', 2)
        cmds.setAttr(plusMinusAverage_bck + '.operation', 2)
        cmds.setAttr(plusMinusAverage_out + '.operation', 2)
        cmds.setAttr(plusMinusAverage_in + '.operation', 2)

        cmds.setAttr(pointMatrixMult_node + '.inPoint', 1, 0, 0)
        cmds.setAttr(pointMatrixMult_node + '.vectorMultiply', 1)
        cmds.connectAttr(obj + '.matrix', pointMatrixMult_node + '.inMatrix')
        cmds.connectAttr(pointMatrixMult_node + '.output', angleBetween_angle_node + '.vector1')
        cmds.setAttr(angleBetween_angle_node + '.vector2', 1, 0, 0)
        cmds.connectAttr(angleBetween_angle_node + '.angle', obj + '.angle')

        cmds.setAttr(angleBetween_direction_node + '.vector1', 0, 0, 0)
        cmds.setAttr(angleBetween_direction_node + '.vector2', 0, 1, 0)
        cmds.connectAttr(pointMatrixMult_node + '.outputY', angleBetween_direction_node + '.vector1Y')
        cmds.connectAttr(pointMatrixMult_node + '.outputZ', angleBetween_direction_node + '.vector1Z')
        cmds.connectAttr(angleBetween_direction_node + '.angle', plusMinusAverage_node + '.input1D[1]')
        cmds.setAttr(plusMinusAverage_node + '.input1D[0]', 360)
        cmds.setAttr(plusMinusAverage_node + '.operation', 2)
        cmds.connectAttr(plusMinusAverage_node + '.output1D', condition_node + '.colorIfTrueR')
        cmds.connectAttr(angleBetween_direction_node + '.angle', condition_node + '.colorIfFalseR')
        cmds.connectAttr(pointMatrixMult_node + '.outputZ', condition_node + '.firstTerm')
        cmds.setAttr(condition_node + '.operation', 2)
        cmds.connectAttr(condition_node + '.outColorR', obj + '.direction')
        # 设置驱动关键帧
        rotate180_keyframe_values = [0, 1]
        rotate180_driver_values = [0, 180]
        for i in range(len(rotate180_driver_values)):
            cmds.setDrivenKeyframe(
                obj,
                attribute='rotate180',
                currentDriver=obj + '.angle',
                driverValue=rotate180_driver_values[i],
                value=rotate180_keyframe_values[i],
                inTangentType='linear',
                outTangentType='linear'
            )
        direction0_keyframe_values = [1, 0, 0, 1]
        direction0_driver_values = [0, 90, 270, 360]
        for i in range(len(direction0_driver_values)):
            cmds.setDrivenKeyframe(
                obj,
                attribute='direction0',
                currentDriver=obj + '.direction',
                driverValue=direction0_driver_values[i],
                value=direction0_keyframe_values[i],
                inTangentType='linear',
                outTangentType='linear'
            )
        direction90_keyframe_values = [0, 1, 0]
        direction90_driver_values = [0, 90, 180]
        for i in range(len(direction90_driver_values)):
            cmds.setDrivenKeyframe(
                obj,
                attribute='direction90',
                currentDriver=obj + '.direction',
                driverValue=direction90_driver_values[i],
                value=direction90_keyframe_values[i],
                inTangentType='linear',
                outTangentType='linear'
            )
        direction180_keyframe_values = [0, 1, 0]
        direction180_driver_values = [90, 180, 270]
        for i in range(len(direction180_driver_values)):
            cmds.setDrivenKeyframe(
                obj,
                attribute='direction180',
                currentDriver=obj + '.direction',
                driverValue=direction180_driver_values[i],
                value=direction180_keyframe_values[i],
                inTangentType='linear',
                outTangentType='linear'
            )
        direction270_keyframe_values = [0, 1, 0]
        direction270_driver_values = [180, 270, 360]
        for i in range(len(direction270_driver_values)):
            cmds.setDrivenKeyframe(
                obj,
                attribute='direction270',
                currentDriver=obj + '.direction',
                driverValue=direction270_driver_values[i],
                value=direction270_keyframe_values[i],
                inTangentType='linear',
                outTangentType='linear'
            )
        # 创建相乘节点
        multDoubleLinear0 = cmds.createNode('multDoubleLinear')
        multDoubleLinear90 = cmds.createNode('multDoubleLinear')
        multDoubleLinear180 = cmds.createNode('multDoubleLinear')
        multDoubleLinear270 = cmds.createNode('multDoubleLinear')
        # 连接相乘节点0
        cmds.connectAttr(obj + '.rotate180', multDoubleLinear0 + '.input1')
        cmds.connectAttr(obj + '.direction0', multDoubleLinear0 + '.input2')
        cmds.connectAttr(multDoubleLinear0 + '.output', plusMinusAverage_fwd + '.input1D[0]')
        cmds.connectAttr(multDoubleLinear180 + '.output', plusMinusAverage_fwd + '.input1D[1]')
        cmds.connectAttr(plusMinusAverage_fwd + '.output1D', obj + '.drivenFwd')
        # 连接相乘节点90
        cmds.connectAttr(obj + '.rotate180', multDoubleLinear90 + '.input1')
        cmds.connectAttr(obj + '.direction90', multDoubleLinear90 + '.input2')
        cmds.connectAttr(multDoubleLinear90 + '.output', plusMinusAverage_out + '.input1D[0]')
        cmds.connectAttr(multDoubleLinear270 + '.output', plusMinusAverage_out + '.input1D[1]')
        cmds.connectAttr(plusMinusAverage_out + '.output1D', obj + '.drivenOut')
        # 连接相乘节点180
        cmds.connectAttr(obj + '.rotate180', multDoubleLinear180 + '.input1')
        cmds.connectAttr(obj + '.direction180', multDoubleLinear180 + '.input2')
        cmds.connectAttr(multDoubleLinear180 + '.output', plusMinusAverage_bck + '.input1D[0]')
        cmds.connectAttr(multDoubleLinear0 + '.output', plusMinusAverage_bck + '.input1D[1]')
        cmds.connectAttr(plusMinusAverage_bck + '.output1D', obj + '.drivenBck')
        # 连接相乘节点270
        cmds.connectAttr(obj + '.rotate180', multDoubleLinear270 + '.input1')
        cmds.connectAttr(obj + '.direction270', multDoubleLinear270 + '.input2')
        cmds.connectAttr(multDoubleLinear270 + '.output', plusMinusAverage_in + '.input1D[0]')
        cmds.connectAttr(multDoubleLinear90 + '.output', plusMinusAverage_in + '.input1D[1]')
        cmds.connectAttr(plusMinusAverage_in + '.output1D', obj + '.drivenIn')

        # 结束记录撤销信息
        cmds.undoInfo(closeChunk=True)
    '''
    将旋转置于关节方向
    '''
    def rotate_to_jointOrient(self):
        selectObjs = cmds.ls(selection=True)
        for obj in selectObjs:
            if cmds.nodeType(obj)=='joint':
                rotate = cmds.xform(obj,q=True,rotation=True)
                cmds.setAttr(f'{obj}.jointOrientX',rotate[0])
                cmds.setAttr(f'{obj}.jointOrientY', rotate[1])
                cmds.setAttr(f'{obj}.jointOrientZ', rotate[2])
    '''
    按层级排列
    '''
    def hierarchy_ordered(self,objs):

        hierarchy = []#结果
        queue = []
        objs_set = set(objs)

        for obj in objs:
            long_name = cmds.ls(obj, long=True)[0]
            parents = long_name.split('|')[1:-1]
            if not any(parent in objs for parent in parents) or parents == []:  # 获取所有顶层物体
                queue.append(obj)
        while queue:
            current_obj = queue.pop(0)  # 从队列中移除最前面的关节
            if current_obj in objs_set and current_obj not in hierarchy:
                hierarchy.append(current_obj)  # 添加到层级列表中

            # 获取当前物体的子级
            children = cmds.listRelatives(current_obj, children=True) or []
            # 按照层级顺序，将子物体添加到队列
            for child in children:
                if child not in queue:
                    queue.append(child)
        return hierarchy

    '''
    创建控制器
    '''
    def create_ctrl(self):
        select_objs = cmds.ls(selection=True)
        if select_objs==[]:
            cmds.warning('需要选中被驱动的物体')
            return
        objs = self.hierarchy_ordered(select_objs)
        for obj in objs:
            parts = obj.split('_')
            if len(parts)>=3:
                name =parts[1]+'_'+parts[0]+'_'+parts[2]
            elif len(parts)==2:
                name = parts[1] + '_' + parts[0]
            else:
                name = parts[0]
            zero = cmds.createNode('transform', name=f'zero_{name}')
            driven = cmds.createNode('transform', name=f'driven_{name}')
            child_joints = cmds.listRelatives(obj, children=True, type='joint')
            child_joint = child_joints[0] if child_joints else ''
            dis = 2
            if child_joint:
                dis = self.calculate_distance(obj,child_joint)
            else:
                dis = dis
            crv = cmds.curve(
                d=1,
                p=[(0, 2, 2), (0, 2, -2), (dis, 2, -2), (dis, 2, 2),
                   (0, 2, 2), (0, -2, 2), (0, -2, -2), (0, 2, -2),
                   (0, 2, 2), (0, -2, 2), (dis, -2, 2), (dis, 2, 2),
                   (dis, 2, -2), (dis, -2, -2), (dis, -2, 2), (dis, -2, -2),
                   (0, -2, -2)],
                k=list(range(17))
            )
            ctrl = f'ctrl_{name}'
            cmds.rename(crv, ctrl)
            cmds.matchTransform(zero, obj)
            cmds.matchTransform(driven, obj)
            cmds.matchTransform(ctrl, obj)
            cmds.parent(ctrl, driven)
            cmds.parent(driven, zero)
            cmds.setAttr(f'{ctrl}.v',channelBox=True,keyable=True)
            self.parentCon(ctrl, obj)
            if self.cb01_isChecked:
                cmds.scaleConstraint(ctrl, obj)
            else:
                self.setAttrAdv(ctrl,['scaleX','scaleY','scaleZ'],channelBox=False,keyable=False,lock=True)
            parent_joints = cmds.listRelatives(obj, parent=True, type='joint')
            parent_joint = parent_joints[0] if parent_joints else ''
            parent_parts = parent_joint.split('_')
            if len(parent_parts)>=3:
                parent_name = 'ctrl_'+parent_parts[1] + '_' + parent_parts[0] + '_' + parent_parts[2]
            elif len(parent_parts) == 2:
                parent_name = 'ctrl_' + parent_parts[1] + '_' + parent_parts[0]
            else:
                parent_name = 'ctrl_' + parent_parts[0]
            if cmds.objExists(parent_name):
                self.safe_parent(zero,parent_name)
            if self.cb02_isChecked:
                if cmds.objExists('ctrl_c_root'):
                    cmds.addAttr(ctrl,attributeType='float', longName='rotateFollow',maxValue=1, minValue=0,keyable=True,niceName='旋转跟随')
                    pc_name = self.parentCon(['ctrl_c_root',zero],driven,offset=True,skipTranslate=True)
                    rev = cmds.createNode('reverse',name = f'rev_{name}')
                    cmds.connectAttr(f'{ctrl}.rotateFollow',f'{pc_name}.zero_{name}W1')
                    cmds.connectAttr(f'{ctrl}.rotateFollow',f'{rev}.inputX')
                    cmds.connectAttr(f'{rev}.outputX',f'{pc_name}.ctrl_c_rootW0')
                else:
                    cmds.warning('没有找到根控制器：ctrl_c_root')
'''
待办事项
1.躯干拉伸开关
2.拉伸保持体积
3.局部缩放
'''


