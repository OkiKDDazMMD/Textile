bl_info = {
	"name": "Textile",					# プラグイン名
	"author": "Oki_KD",							# 制作者名
	"version": (0, 1),							# バージョン
	"blender": (2, 80, 0),						# 動作可能なBlenderバージョン
	"support": "TESTING",						# サポートレベル
	"category": "3D View",						# カテゴリ名
	"location": "View3D > Sidebar > Textile",	# ロケーション
	"description": "Add Plane",					# 説明文
	"location": "",								# 機能の位置付け
	"warning": "",								# 注意点やバグ情報
	"doc_url": "",								# ドキュメントURL
}


import math
import bpy
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import *


rhombusPoints=[( 0.8,  0.0,  0.0),
			( 1.6,  0.0,  0.6),
			( 0.8,  0.0,  1.2),
			( 0.0,  0.0,  0.6)]
rhombusFaces=[(0,1,2,3)]

rhombusEdgeYPoints=[( 2.4,  0.0,  1.2),
			( 2.4,  0.0,  0.0),
			( 1.6,  0.0,  0.0),
			( 1.6,  0.0,  0.6)]
rhombusEdgeYFaces=[(0,1,2,3)]

rhombusEdgeXPoints=[( 0.0,  0.0,  1.2),
			( 0.8,  0.0,  1.2),
			( 1.6,  0.0,  0.6),
			( 0.0,  0.0,  0.6)]
rhombusEdgeXFaces=[(0,1,2,3)]

rhombusEdgeXYPoints=[( 0.0,  0.0,  0.0),
			( 1.6,  0.0,  0.0),
			( 1.6,  0.0,  0.6),
			( 0.0,  0.0,  0.6)]
rhombusEdgeXYFaces=[(0,1,2,3)]


miuraOriPoints=[(0.1,  0.0,  0.0),
			( 0.9,  0.0,  0.0),
			( 0.8,  0.0,  0.92),
			( 0.0,  0.0,  0.92),
			( 0.9,  0.0,  1.84),
			( 0.1,  0.0,  1.84)]
miuraOriFaces=[(0,1,2,3), (3,2,4,5)]

miuraOriEdgeX0Points=[(0.0,  0.0,  0.0),
			( 0.9,  0.0,  0.0),
			( 0.8,  0.0,  0.92),
			( 0.0,  0.0,  0.92),
			( 0.9,  0.0,  1.84),
			( 0.0,  0.0,  1.84)]
miuraOriEdgeX0Faces=[(0,1,2,3), (3,2,4,5)]

miuraOriEdgeX1Points=[(0.1,  0.0,  0.0),
			( 0.9,  0.0,  0.0),
			( 0.9,  0.0,  0.92),
			( 0.0,  0.0,  0.92),
			( 0.9,  0.0,  1.84),
			( 0.1,  0.0,  1.84)]
miuraOriEdgeX1Faces=[(0,1,2,3), (3,2,4,5)]


miuraOri2Points=[(0.1,  0.0,  0.0),
			( 0.9,  0.0,  0.09),
			( 0.8,  0.0,  1.01),
			( 0.0,  0.0,  0.92),
			( 0.9,  0.0,  1.93),
			( 0.1,  0.0,  1.84),
			( 1.7,  0.0,  0.0),
			( 1.6,  0.0,  0.92),
			( 1.7,  0.0,  1.84)]
miuraOri2Faces=[(0,1,2,3), (3,2,4,5), (1,6,7,2), (2,7,8,4)]

miuraOri2EdgeX0Points=[(0.0,  0.0,  1.01),
			( 0.9,  0.0,  0.92),
			( 0.8,  0.0,  1.84),
			( 0.0,  0.0,  1.93),
			( 0.9,  0.0,  2.76),
			( 0.0,  0.0,  2.85)]
miuraOri2EdgeX0Faces=[(0,1,2,3), (3,2,4,5)]

miuraOri2EdgeX1Points=[(0.1,  0.0,  0.92),
			( 0.9,  0.0,  1.01),
			( 0.9,  0.0,  1.93),
			( 0.0,  0.0,  1.84),
			( 0.9,  0.0,  2.85),
			( 0.1,  0.0,  2.76)]
miuraOri2EdgeX1Faces=[(0,1,2,3), (3,2,4,5)]

miuraOri2EdgeY0Points=[(0.8,  0.0,  0.0),
			( 1.6,  0.0,  0.0),
			( 1.7,  0.0,  1.01),
			( 0.9,  0.0,  0.92),
			( 2.4,  0.0,  0.0),
			( 2.5,  0.0,  0.92)]
miuraOri2EdgeY0Faces=[(0,1,2,3), (2,1,4,5)]

miuraOri2EdgeY1Points=[(0.9,  0.0,  0.0),
			( 1.7,  0.0,  0.09),
			( 1.6,  0.0,  1.01),
			( 0.8,  0.0,  1.01),
			( 2.5,  0.0,  0.0),
			( 2.4,  0.0,  1.01)]
miuraOri2EdgeY1Faces=[(0,1,2,3), (2,1,4,5)]

miuraOri2EdgeX0Y0Points=[(0.0,  0.0,  0.0),
			( 0.8,  0.0,  0.0),
			( 0.9,  0.0,  0.92),
			( 0.0,  0.0,  1.01)]
miuraOri2EdgeX0Y0Faces=[(0,1,2,3)]

miuraOri2EdgeX1Y0Points=[(0.0,  0.0,  0.0),
			( 0.9,  0.0,  0.0),
			( 0.9,  0.0,  1.01),
			( 0.1,  0.0,  0.92)]
miuraOri2EdgeX1Y0Faces=[(0,1,2,3)]

miuraOri2EdgeX0Y1Points=[(0.0,  0.0,  0.09),
			( 0.9,  0.0,  0.0),
			( 0.8,  0.0,  1.01),
			( 0.0,  0.0,  1.01)]
miuraOri2EdgeX0Y1Faces=[(0,1,2,3)]

miuraOri2EdgeX1Y1Points=[(0.1,  0.0,  0.0),
			( 0.9,  0.0,  0.09),
			( 0.9,  0.0,  1.01),
			( 0.0,  0.0,  1.01)]
miuraOri2EdgeX1Y1Faces=[(0,1,2,3)]


honeycombPoints=[( 0.5,  0.0,  0.0),
			( 1.5,  0.0,  0.0),
			( 2.0,  0.0,  0.8),
			( 1.5,  0.0,  1.6),
			( 0.5,  0.0,  1.6),
			( 0.0,  0.0,  0.8),
			( 3.0,  0.0,  0.8),
			( 2.0,  0.0,  2.4),
			( 3.5,  0.0,  1.6),
			( 3.0,  0.0,  2.4)]
honeycombFaces=[(0,1,2,3), (0,3,4,5), (3,2,6,7), (7,6,8,9)]

honeycombEdgeY0Points=[(2.5,  0.0,  0.0),
			( 4.5,  0.0,  0.0),
			( 4.0,  0.0,  0.8),
			( 3.0,  0.0,  0.8)]
honeycombEdgeY0Faces=[(0,1,2,3)]

honeycombEdgeY1Points=[(1.5,  0.0,  0.0),
			( 2.5,  0.0,  0.0),
			( 3.0,  0.0,  0.8),
			( 1.0,  0.0,  0.8)]
honeycombEdgeY1Faces=[(0,1,2,3)]

honeycombEdgeX0APoints=[(0.0,  0.0,  0.0),
			( 1.5,  0.0,  0.0),
			( 1.0,  0.0,  0.8),
			( 0.0,  0.0,  0.8)]
honeycombEdgeX0AFaces=[(0,1,2,3)]

honeycombEdgeX0BPoints=[(0.0,  0.0,  0.0),
			( 4.5,  0.0,  0.0),
			( 4.0,  0.0,  0.8),
			( 3.0,  0.0,  0.8)]
honeycombEdgeX0BFaces=[(0,1,2,3)]


honeycomb2Points=[( 0.5,  0.0,  0.0),
			( 1.5,  0.0,  0.0),
			( 2.0,  0.0,  0.8),
			( 0.0,  0.0,  0.8),
			( 1.5,  0.0,  1.6),
			( 0.5,  0.0,  1.6)]
honeycomb2Faces=[(0,1,2,3), (3,2,4,5)]


def height_Update(self, context):
	if self.count_Height < 2:
		self.count_Height = 2

	if self.prop_Enum == "MiuraOri":
		length = (self.count_Height) * 1.84

	elif self.prop_Enum == "MiuraOri2":
		length = (self.count_Height) * 1.84 + 0.09
		if context.scene.okikd_textile_property.prop_Bool:
			length = length + 1.84

	elif self.prop_Enum == "Rhombus":
		length = (self.count_Height) * 1.2 + 0.6
		if context.scene.okikd_textile_property.prop_Bool:
			length = length + 1.8

	elif self.prop_Enum == "Square":
		length = self.count_Height

	else:
		length = (self.count_Height) * 1.6 + 0.8

	if length>=100.0:
		self.prop_HeightString = "%s m" % (length/100.0)
	else:
		self.prop_HeightString = "%s cm" % (length)


def width_Update(self, context):
	if self.count_Width < 2:
		self.count_Width = 2

	if self.prop_Enum == "MiuraOri":
		length = (self.count_Width) * 0.8 + 0.1
		if context.scene.okikd_textile_property.prop_Bool:
			length = length + 1.6

	elif self.prop_Enum == "MiuraOri2":
		length = (self.count_Width) * 1.6 + 0.1
		if context.scene.okikd_textile_property.prop_Bool:
			length = length + 1.6

	elif self.prop_Enum == "Rhombus":
		length = (self.count_Width) * 1.6 + 0.8
		if context.scene.okikd_textile_property.prop_Bool:
			length = length + 2.4

	elif self.prop_Enum == "Square":
		length = self.count_Width

	else:
		length = (self.count_Width) * 3.0 + 0.5
		if context.scene.okikd_textile_property.prop_Bool:
			length = length + 1.0

	if length>=100.0:
		self.prop_WidthString = "%s m" % (length/100.0)
	else:
		self.prop_WidthString = "%s cm" % (length)


def bool_Update(self, context):
	height_Update(self, context)
	width_Update(self, context)


def enum_Update(self, context):
	if self.prop_Enum == "MiuraOri":
		self.count_Height = 43
		if context.scene.okikd_textile_property.prop_Bool:
			self.count_Width = 60
		else:
			self.count_Width = 62

	elif self.prop_Enum == "MiuraOri2":
		self.count_Height = 43
		if context.scene.okikd_textile_property.prop_Bool:
			self.count_Width = 30
		else:
			self.count_Width = 31

	elif self.prop_Enum == "Rhombus":
		if context.scene.okikd_textile_property.prop_Bool:
			self.count_Height = 65
			self.count_Width = 29
		else:
			self.count_Height = 66
			self.count_Width = 31

	elif self.prop_Enum == "Square":
		self.count_Height = 80
		self.count_Width = 50

	else:
		self.count_Height = 50
		self.count_Width = 16

	bool_Update(self, context)


# Panel
class UI(bpy.types.Panel):
	bl_label = "Textile"
	bl_idname = "id.testpanel"
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"
	bl_category = "Textile"
	
	def draw(self,context):
		# UI に配置
		self.layout.prop(context.scene.okikd_textile_property, "prop_Enum")
		self.layout.prop(context.scene.okikd_textile_property, "count_Height")
		self.layout.prop(context.scene.okikd_textile_property, "count_Width")
		self.layout.prop(context.scene.okikd_textile_property, "prop_Bool")
		self.layout.prop(context.scene.okikd_textile_property, "prop_HeightString")
		self.layout.prop(context.scene.okikd_textile_property, "prop_WidthString")
		self.layout.operator("addplane.button")


# 実行ボタン
class Button(bpy.types.Operator):
	bl_idname = "addplane.button"
	bl_label = "Add Plane"

	# オブジェクト作成
	def createObj(self, nameObj, points, faces):
		# 新規メッシュを作成
		mesh = bpy.data.meshes.new(name="%sMesh" % nameObj)
		# メッシュの頂点、辺、面を埋める
		mesh.from_pydata(points,[],faces)
		# 新たなデータでメッシュを更新
		mesh.update(calc_edges=True)
		# メッシュでオブジェクトを作成
		obj = bpy.data.objects.new(name=nameObj, object_data=mesh)
		# オブジェクトをシーンにリンク
		bpy.context.scene.collection.objects.link(obj)
		bpy.context.view_layer.objects.active = obj
		# 返値 
		return obj

	# オブジェクト複製
	def copyObj(self, obj):
		obj_copy = obj.copy()
		obj_copy.data = obj_copy.data.copy()
		bpy.context.scene.collection.objects.link(obj_copy)
		bpy.context.view_layer.objects.active = obj_copy
		return obj_copy

	# 配列複製モディファイア
	def modifierArray(self, count, OffsetX=0.0, OffsetZ=0.0):
		bpy.ops.object.modifier_add(type='ARRAY')
		bpy.context.object.modifiers["配列"].count = count
		bpy.context.object.modifiers["配列"].use_relative_offset = False
		bpy.context.object.modifiers["配列"].use_constant_offset = True
		bpy.context.object.modifiers["配列"].constant_offset_displace[0] = OffsetX
		bpy.context.object.modifiers["配列"].constant_offset_displace[2] = OffsetZ
		bpy.context.object.modifiers["配列"].use_merge_vertices = True
		bpy.ops.object.modifier_apply(modifier="配列")

	# オブジェクトを統合
	def joinObj(self):
		bpy.ops.object.select_all(action='SELECT')
		bpy.ops.object.join()
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_all(action='SELECT')
		bpy.ops.mesh.remove_doubles()

	# Honeycombでの外枠面を作成
	def createHoneycombEdge(self, context):
		# 作成平面を移動
		bpy.context.object.location[0] = 1.0
		# Y=0 側の外枠面を作成
		self.createObj("honeycombEdgeY0", honeycombEdgeY0Points, honeycombEdgeY0Faces)
		self.modifierArray(context.scene.okikd_textile_property.count_Width, 3.0, 0.0)
		# Y=+ 側の外枠面を作成
		self.createObj("honeycombEdgeY1", honeycombEdgeY1Points, honeycombEdgeY1Faces)
		self.modifierArray(context.scene.okikd_textile_property.count_Width, 3.0, 0.0)
		bpy.context.object.location[2] = 1.6 * context.scene.okikd_textile_property.count_Height
		# X 側の外枠面を作成 
		objX0A = self.createObj("honeycombEdgeX0A", honeycombEdgeX0APoints, honeycombEdgeX0AFaces)
		# X 側の外枠面を構成する面は4パターンで、そのうちの一つが前行で作成した"honeycombEdgeX0A"だが、他の3パターンはこの"honeycombEdgeX0A"をミラー変形する事により作成する事が出来る
		objX0B = self.copyObj(objX0A)
		objX0B.select_set(True)
		bpy.ops.transform.mirror(constraint_axis=(False, False, True))
		bpy.context.object.location[2] = 1.6
		objX0B.select_set(False)

		objX1A = self.copyObj(objX0A)
		objX1A.select_set(True)
		bpy.ops.transform.mirror(constraint_axis=(True, False, False))
		bpy.context.object.location[0] = 3.0 * (context.scene.okikd_textile_property.count_Width) + 2.5
		bpy.context.object.location[2] = 0.8
		objX1A.select_set(False)

		objX1B = self.copyObj(objX0B)
		objX1B.select_set(True)
		bpy.ops.transform.mirror(constraint_axis=(True, False, False))
		bpy.context.object.location[0] = 3.0 * (context.scene.okikd_textile_property.count_Width) + 2.5
		bpy.context.object.location[2] = 0.8
		objX1B.select_set(False)
		# 配列複製
		bpy.context.view_layer.objects.active = objX0A
		self.modifierArray(context.scene.okikd_textile_property.count_Height + 1, 0.0, 1.6)
		bpy.context.view_layer.objects.active = objX0B
		self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, -1.6)
		bpy.context.view_layer.objects.active = objX1A
		self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, 1.6)
		bpy.context.view_layer.objects.active = objX1B
		self.modifierArray(context.scene.okikd_textile_property.count_Height + 1, 0.0, -1.6)
		# オブジェクトを統合
		self.joinObj()
		# 法線の方向を揃える
		bpy.ops.mesh.normals_make_consistent(inside=False)



	def execute(self, context):

		typeplane = context.scene.okikd_textile_property.prop_Enum
		context.scene.okikd_textile_property.prop_String = typeplane

		if typeplane == "Honeycomb":
			self.createObj("Honeycomb", honeycombPoints, honeycombFaces)
			self.modifierArray(context.scene.okikd_textile_property.count_Width, 3.0, 0.0)
			self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, 1.6)
			if context.scene.okikd_textile_property.prop_Bool:
				self.createHoneycombEdge(context)

		elif typeplane == "Honeycomb2":
			self.createObj("Honeycomb2", honeycomb2Points, honeycomb2Faces)
			self.modifierArray(2, 1.5, 0.8)
			self.modifierArray(context.scene.okikd_textile_property.count_Width, 3.0, 0.0)
			self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, 1.6)
			if context.scene.okikd_textile_property.prop_Bool:
				self.createHoneycombEdge(context)


		elif typeplane == "Rhombus":
			self.createObj("Rhombus", rhombusPoints, rhombusFaces)
			self.modifierArray(2, 0.8, 0.6)
			self.modifierArray(context.scene.okikd_textile_property.count_Width, 1.6, 0.0)
			self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, 1.2)
			# 外枠の面を作成
			if context.scene.okikd_textile_property.prop_Bool:
				self.createObj("Rhombus1", rhombusPoints, rhombusFaces)
				self.modifierArray(context.scene.okikd_textile_property.count_Width + 1, 1.6, 0.0)
				bpy.context.object.location[2] = (context.scene.okikd_textile_property.count_Height) * 1.2
				self.createObj("Rhombus2", rhombusPoints, rhombusFaces)
				self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, 1.2)
				bpy.context.object.location[0] = (context.scene.okikd_textile_property.count_Width) * 1.6
				# オブジェクトを統合
				self.joinObj()
				# 作成平面を移動
				bpy.context.object.location[2] = 0.6
				bpy.context.object.location[0] = (context.scene.okikd_textile_property.count_Width) * 1.6 + 0.8
				# Y 側の外枠面を作成
				# Y=0 側の外枠面を作成
				self.createObj("RhombusEdgeY00", rhombusEdgeYPoints, rhombusEdgeYFaces)
				self.modifierArray(context.scene.okikd_textile_property.count_Width, 1.6, 0.0)

				objY01 = self.createObj("RhombusEdgeY01", rhombusEdgeYPoints, rhombusEdgeYFaces)
				bpy.ops.object.select_all(action='DESELECT')
				objY01.select_set(True)
				bpy.ops.transform.mirror(constraint_axis=(True, False, False))
				objY01.location[0] = 4.8
				# 2行前で鏡面移動しているため　-1.6　とオフセット値で負の値を入れなければならない
				self.modifierArray(context.scene.okikd_textile_property.count_Width, -1.6, 0.0)
				# Y=+ 側の外枠面を作成
				objY10 = self.createObj("RhombusEdgeY10", rhombusEdgeYPoints, rhombusEdgeYFaces)
				bpy.ops.object.select_all(action='DESELECT')
				objY10.select_set(True)
				bpy.ops.transform.mirror(constraint_axis=(False, False, True))
				objY10.location[2] = (context.scene.okikd_textile_property.count_Height + 2) * 1.2
				self.modifierArray(context.scene.okikd_textile_property.count_Width, 1.6, 0.0)

				objY11 = self.createObj("RhombusEdgeY11", rhombusEdgeYPoints, rhombusEdgeYFaces)
				bpy.ops.object.select_all(action='DESELECT')
				objY11.select_set(True)
				bpy.ops.transform.mirror(constraint_axis=(True, False, True))
				objY11.location[0] = 4.8
				objY11.location[2] = (context.scene.okikd_textile_property.count_Height + 2) * 1.2
				self.modifierArray(context.scene.okikd_textile_property.count_Width, -1.6, 0.0)

				# X 側の外枠面を作成
				# X=0 側の外枠面を作成
				self.createObj("RhombusEdgeX00", rhombusEdgeXPoints, rhombusEdgeXFaces)
				self.modifierArray(context.scene.okikd_textile_property.count_Height + 1, 0.0, 1.2)

				objX01 = self.createObj("RhombusEdgeX01", rhombusEdgeXPoints, rhombusEdgeXFaces)
				bpy.ops.object.select_all(action='DESELECT')
				objX01.select_set(True)
				bpy.ops.transform.mirror(constraint_axis=(False, False, True))
				objX01.location[2] = 2.4
				self.modifierArray(context.scene.okikd_textile_property.count_Height + 1, 0.0, -1.2)
				# X=+ 側の外枠面を作成
				objX10 = self.createObj("RhombusEdgeX10", rhombusEdgeXPoints, rhombusEdgeXFaces)
				bpy.ops.object.select_all(action='DESELECT')
				objX10.select_set(True)
				bpy.ops.transform.mirror(constraint_axis=(True, False, False))
				objX10.location[0] = (context.scene.okikd_textile_property.count_Width + 2) * 1.6
				self.modifierArray(context.scene.okikd_textile_property.count_Height + 1, 0.0, 1.2)

				objX11 = self.createObj("RhombusEdgeX11", rhombusEdgeXPoints, rhombusEdgeXFaces)
				bpy.ops.object.select_all(action='DESELECT')
				objX11.select_set(True)
				bpy.ops.transform.mirror(constraint_axis=(True, False, True))
				objX11.location[2] = 2.4
				objX11.location[0] = (context.scene.okikd_textile_property.count_Width + 2) * 1.6
				self.modifierArray(context.scene.okikd_textile_property.count_Height + 1, 0.0, -1.2)
				# 四隅の面を作成
				self.createObj("RhombusEdgeXY", rhombusEdgeXYPoints, rhombusEdgeXYFaces)
				self.modifierArray(2, (context.scene.okikd_textile_property.count_Width + 1) * 1.6, 0.0)
				self.modifierArray(2, 0.0, (context.scene.okikd_textile_property.count_Height + 1) * 1.2 + 0.6)
				# オブジェクトを統合
				self.joinObj()
				# 法線の方向を揃える
				bpy.ops.mesh.normals_make_consistent(inside=False)


		elif typeplane == "MiuraOri":
			self.createObj("MiuraOri", miuraOriPoints, miuraOriFaces)
			self.modifierArray(context.scene.okikd_textile_property.count_Width, 0.8, 0.0)
			self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, 1.84)
			# 外枠の面を作成
			if context.scene.okikd_textile_property.prop_Bool:
				# 作成平面を移動
				bpy.context.object.location[0] = 0.8
				# X=0 側の外枠面を作成
				self.createObj("MiuraOriEdgeX0", miuraOriEdgeX0Points, miuraOriEdgeX0Faces)
				self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, 1.84)
				# X=+ 側の外枠面を作成
				self.createObj("MiuraOriEdgeX1", miuraOriEdgeX1Points, miuraOriEdgeX1Faces)
				self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, 1.84)
				bpy.context.object.location[0] = 0.8 * context.scene.okikd_textile_property.count_Width + 0.8
				# オブジェクトを統合
				self.joinObj()


		elif typeplane == "MiuraOri2":
			self.createObj("MiuraOri2", miuraOri2Points, miuraOri2Faces)
			self.modifierArray(context.scene.okikd_textile_property.count_Width, 1.6, 0.0)
			self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, 1.84)
			if context.scene.okikd_textile_property.prop_Bool:
				# 作成平面を移動
				bpy.context.object.location[0] = 0.8
				bpy.context.object.location[2] = 0.92
				# X=0 側の外枠面を作成
				self.createObj("MiuraOri2EdgeX0", miuraOri2EdgeX0Points, miuraOri2EdgeX0Faces)
				cHeight = context.scene.okikd_textile_property.count_Height
				self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, 1.84)
				# X=+ 側の外枠面を作成
				self.createObj("MiuraOri2EdgeX1", miuraOri2EdgeX1Points, miuraOri2EdgeX1Faces)
				cHeight = context.scene.okikd_textile_property.count_Height
				self.modifierArray(context.scene.okikd_textile_property.count_Height, 0.0, 1.84)
				bpy.context.object.location[0] = 1.6 * context.scene.okikd_textile_property.count_Width + 0.8
				# Y=0 側の外枠面を作成
				self.createObj("MiuraOri2EdgeY0", miuraOri2EdgeY0Points, miuraOri2EdgeY0Faces)
				self.modifierArray(context.scene.okikd_textile_property.count_Width, 1.6, 0.0)
				# Y=+ 側の外枠面を作成
				self.createObj("MiuraOri2EdgeY1", miuraOri2EdgeY1Points, miuraOri2EdgeY1Faces)
				self.modifierArray(context.scene.okikd_textile_property.count_Width, 1.6, 0.0)
				bpy.context.object.location[2] = 1.84 * context.scene.okikd_textile_property.count_Height + 0.92
				# 四隅の X=0 Y=0 側を作成
				self.createObj("MiuraOri2EdgeX0Y0", miuraOri2EdgeX0Y0Points, miuraOri2EdgeX0Y0Faces)
				# 四隅の X=+ Y=0 側を作成
				self.createObj("MiuraOri2EdgeX1Y0", miuraOri2EdgeX1Y0Points, miuraOri2EdgeX1Y0Faces)
				bpy.context.object.location[0] = 1.6 * context.scene.okikd_textile_property.count_Width + 0.8
				# 四隅の X=0 Y=+ 側を作成
				self.createObj("MiuraOri2EdgeX0Y1", miuraOri2EdgeX0Y1Points, miuraOri2EdgeX0Y1Faces)
				bpy.context.object.location[2] = 1.84 * context.scene.okikd_textile_property.count_Height + 0.92
				# 四隅の X=+ Y=+ 側を作成
				self.createObj("MiuraOri2EdgeX1Y1", miuraOri2EdgeX1Y1Points, miuraOri2EdgeX1Y1Faces)
				bpy.context.object.location[0] = 1.6 * context.scene.okikd_textile_property.count_Width + 0.8
				bpy.context.object.location[2] = 1.84 * context.scene.okikd_textile_property.count_Height + 0.92
				# オブジェクトを統合
				self.joinObj()

		else:
			bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(0.5, 0, 0.5), rotation=(math.radians(90), 0, 0), scale=(1, 1, 1))
			cWidth = context.scene.okikd_textile_property.count_Width
			if cWidth > 1:
				bpy.ops.object.modifier_add(type='ARRAY')
				bpy.context.object.modifiers["配列"].count = cWidth
				bpy.context.object.modifiers["配列"].use_merge_vertices = True
				bpy.ops.object.modifier_apply(modifier="配列")
			bpy.ops.object.modifier_add(type='ARRAY')
			bpy.context.object.modifiers["配列"].count = context.scene.okikd_textile_property.count_Height
			bpy.context.object.modifiers["配列"].relative_offset_displace[0] = 0
			bpy.context.object.modifiers["配列"].relative_offset_displace[1] = 1
			bpy.context.object.modifiers["配列"].use_merge_vertices = True
			bpy.ops.object.modifier_apply(modifier="配列")


		return{'FINISHED'}


# プロパティ
class Property_Textile(PropertyGroup):

	count_Height: IntProperty(
		name="Height",
		default=80,
		update=height_Update
	)

	count_Width: IntProperty(
		name="Width",
		default=50,
		update=width_Update
	)

	prop_Bool: BoolProperty(
		name="Align the edge", 
		update=bool_Update,
		default=True,
	)
	
	prop_HeightString: StringProperty(
		name="Height Length",
		default="80 cm",
	)

	prop_WidthString: StringProperty(
		name="Width Length",
		default="50 cm",
	)

	prop_Enum: EnumProperty(
		name="Type",
 		default="Square",
		update=enum_Update,
		items= [ 
				("Square","Square","Square"),
				("Honeycomb","Honeycomb","Honeycomb"),
				("Honeycomb2","Honeycomb2","Honeycomb2"),
				("Rhombus","Rhombus","Rhombus"),
				("MiuraOri","MiuraOri","MiuraOri"),
				("MiuraOri2","MiuraOri2","MiuraOri2"),]
	)




classes = (
	UI,
	Button,
	Property_Textile
)


def register():
	for clas in classes:
		bpy.utils.register_class(clas)
	bpy.types.Scene.okikd_textile_property = PointerProperty(type=Property_Textile)


def unregister():
	del bpy.types.Scene.okikd_textile_property
	for clas in reversed(classes):
		bpy.utils.register_class(clas)


if __name__ == "__main__":
	register()
	