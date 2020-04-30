App.newDocument("Project")
App.setActiveDocument("Project")

from FreeCAD import Base
import Part,PartGui,Draft

sketch01 = App.activeDocument().addObject('Sketcher::SketchObject','Sketch01')
sketch01.Placement = App.Placement(App.Vector(0.000000,0.000000,0.000000),App.Rotation(0.000000,0.000000,0.000000,1.000000))

sketch01.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),30),False)
sketch01.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 

sketch01.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),15),False)
sketch01.addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1)) 

sketch01.addGeometry(Part.Circle(App.Vector(8,-21,0),App.Vector(0,0,1),8),False)
sketch01.addSymmetric([2],-2,0) 

sketch01.trim(3,App.Vector(-4.671036,-13.775558,0))
sketch01.trim(2,App.Vector(4.397662,-13.864904,0))
sketch01.trim(3,App.Vector(-1.186513,-16.455961,0))
sketch01.trim(2,App.Vector(0.090503,-19.139975,0))
sketch01.trim(3,App.Vector(-11.270746,-28.304337,0))
sketch01.trim(2,App.Vector(10.701625,-28.702028,0))
sketch01.trim(0,App.Vector(-17.697254,-24.176645,0))
sketch01.trim(1,App.Vector(1.574561,15.313293,0))
sketch01.trim(1,App.Vector(0.207600,14.282619,0))

sketch02 = App.activeDocument().addObject('Sketcher::SketchObject','Sketch02')
sketch02.Placement = App.Placement(App.Vector(0.000000,0.000000,-15),App.Rotation(0.000000,0.000000,0.000000,1.000000))

sketch02.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),30),False)
sketch02.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 

sketch02.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),15),False)
sketch02.addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1)) 

sketch02.addGeometry(Part.Circle(App.Vector(8,-21,0),App.Vector(0,0,1),8),False)
sketch02.addSymmetric([2],-2,0) 

sketch02.trim(3,App.Vector(-4.671036,-13.775558,0))
sketch02.trim(2,App.Vector(4.397662,-13.864904,0))
sketch02.trim(3,App.Vector(-1.186513,-16.455961,0))
sketch02.trim(2,App.Vector(0.090503,-19.139975,0))
sketch02.trim(3,App.Vector(-11.270746,-28.304337,0))
sketch02.trim(2,App.Vector(10.701625,-28.702028,0))
sketch02.trim(0,App.Vector(-17.697254,-24.176645,0))
sketch02.trim(1,App.Vector(1.574561,15.313293,0))
sketch02.trim(1,App.Vector(0.207600,14.282619,0))

App.ActiveDocument.recompute()

scale01 = Draft.scale([sketch01],delta=FreeCAD.Vector(2,2,2),center=FreeCAD.Vector(0,0,0),copy=False)   	#values
scale01.Label = 'Scale01'

scale02 = Draft.scale([sketch02],delta=FreeCAD.Vector(2,2,2),center=FreeCAD.Vector(0,0,0),copy=False)		#values
scale02.Label = 'Scale02'

loft01 = App.getDocument('Project').addObject('Part::Loft','Loft01')
loft01.Sections=[scale01, scale02, ]
loft01.Solid=True
loft01.Ruled=False
loft01.Closed=False

FreeCAD.ActiveDocument.recompute()

FreeCAD.ActiveDocument.recompute()

sketch11 = App.activeDocument().addObject('Sketcher::SketchObject','Sketch11')
sketch11.Placement = App.Placement(App.Vector(0.000000,0.000000,-20),App.Rotation(0.000000,0.000000,0.000000,1.000000))

sketch11.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),30),False)
sketch11.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 

sketch11.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),15),False)
sketch11.addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1)) 

sketch11.addGeometry(Part.Circle(App.Vector(8,-21,0),App.Vector(0,0,1),8),False)
sketch11.addSymmetric([2],-2,0) 

sketch11.trim(3,App.Vector(-4.671036,-13.775558,0))
sketch11.trim(2,App.Vector(4.397662,-13.864904,0))
sketch11.trim(3,App.Vector(-1.186513,-16.455961,0))
sketch11.trim(2,App.Vector(0.090503,-19.139975,0))
sketch11.trim(3,App.Vector(-11.270746,-28.304337,0))
sketch11.trim(2,App.Vector(10.701625,-28.702028,0))
sketch11.trim(0,App.Vector(-17.697254,-24.176645,0))
sketch11.trim(1,App.Vector(1.574561,15.313293,0))
sketch11.trim(1,App.Vector(0.207600,14.282619,0))

sketch12 = App.activeDocument().addObject('Sketcher::SketchObject','Sketch12')
sketch12.Placement = App.Placement(App.Vector(0.000000,0.000000,-35),App.Rotation(0.000000,0.000000,0.000000,1.000000))

sketch12.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),30),False)
sketch12.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 

sketch12.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),15),False)
sketch12.addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1)) 

sketch12.addGeometry(Part.Circle(App.Vector(8,-21,0),App.Vector(0,0,1),8),False)
sketch12.addSymmetric([2],-2,0) 

sketch12.trim(3,App.Vector(-4.671036,-13.775558,0))
sketch12.trim(2,App.Vector(4.397662,-13.864904,0))
sketch12.trim(3,App.Vector(-1.186513,-16.455961,0))
sketch12.trim(2,App.Vector(0.090503,-19.139975,0))
sketch12.trim(3,App.Vector(-11.270746,-28.304337,0))
sketch12.trim(2,App.Vector(10.701625,-28.702028,0))
sketch12.trim(0,App.Vector(-17.697254,-24.176645,0))
sketch12.trim(1,App.Vector(1.574561,15.313293,0))
sketch12.trim(1,App.Vector(0.207600,14.282619,0))

scale11 = Draft.scale([sketch11],delta=FreeCAD.Vector(2,2,2),center=FreeCAD.Vector(0,0,0),copy=False)   	#values
scale11.Label = 'Scale11'

scale12 = Draft.scale([sketch12],delta=FreeCAD.Vector(2,2,2),center=FreeCAD.Vector(0,0,0),copy=False)		#values
scale12.Label = 'Scale12'

loft11 = App.getDocument('Project').addObject('Part::Loft','Loft11')
loft11.Sections=[scale11, scale12, ]
loft11.Solid=True
loft11.Ruled=False
loft11.Closed=False

FreeCAD.ActiveDocument.recompute()

FreeCAD.ActiveDocument.recompute()

sketch21 = App.activeDocument().addObject('Sketcher::SketchObject','Sketch21')
sketch21.Placement = App.Placement(App.Vector(0.000000,0.000000,-40),App.Rotation(0.000000,0.000000,0.000000,1.000000))

sketch21.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),30),False)
sketch21.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 

sketch21.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),15),False)
sketch21.addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1)) 

sketch21.addGeometry(Part.Circle(App.Vector(8,-21,0),App.Vector(0,0,1),8),False)
sketch21.addSymmetric([2],-2,0) 

sketch21.trim(3,App.Vector(-4.671036,-13.775558,0))
sketch21.trim(2,App.Vector(4.397662,-13.864904,0))
sketch21.trim(3,App.Vector(-1.186513,-16.455961,0))
sketch21.trim(2,App.Vector(0.090503,-19.139975,0))
sketch21.trim(3,App.Vector(-11.270746,-28.304337,0))
sketch21.trim(2,App.Vector(10.701625,-28.702028,0))
sketch21.trim(0,App.Vector(-17.697254,-24.176645,0))
sketch21.trim(1,App.Vector(1.574561,15.313293,0))
sketch21.trim(1,App.Vector(0.207600,14.282619,0))

sketch22 = App.activeDocument().addObject('Sketcher::SketchObject','Sketch22')
sketch22.Placement = App.Placement(App.Vector(0.000000,0.000000,-55),App.Rotation(0.000000,0.000000,0.000000,1.000000))

sketch22.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),30),False)
sketch22.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 

sketch22.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),15),False)
sketch22.addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1)) 

sketch22.addGeometry(Part.Circle(App.Vector(8,-21,0),App.Vector(0,0,1),8),False)
sketch22.addSymmetric([2],-2,0) 

sketch22.trim(3,App.Vector(-4.671036,-13.775558,0))
sketch22.trim(2,App.Vector(4.397662,-13.864904,0))
sketch22.trim(3,App.Vector(-1.186513,-16.455961,0))
sketch22.trim(2,App.Vector(0.090503,-19.139975,0))
sketch22.trim(3,App.Vector(-11.270746,-28.304337,0))
sketch22.trim(2,App.Vector(10.701625,-28.702028,0))
sketch22.trim(0,App.Vector(-17.697254,-24.176645,0))
sketch22.trim(1,App.Vector(1.574561,15.313293,0))
sketch22.trim(1,App.Vector(0.207600,14.282619,0))

scale21 = Draft.scale([sketch21],delta=FreeCAD.Vector(2,2,2),center=FreeCAD.Vector(0,0,0),copy=False)   	#values
scale21.Label = 'Scale21'

scale22 = Draft.scale([sketch22],delta=FreeCAD.Vector(2,2,2),center=FreeCAD.Vector(0,0,0),copy=False)		#values
scale22.Label = 'Scale22'

loft21 = App.getDocument('Project').addObject('Part::Loft','Loft21')
loft21.Sections=[scale21, scale22, ]
loft21.Solid=True
loft21.Ruled=False
loft21.Closed=False

FreeCAD.ActiveDocument.recompute()

FreeCAD.ActiveDocument.recompute()

sketch31 = App.activeDocument().addObject('Sketcher::SketchObject','Sketch31')
sketch31.Placement = App.Placement(App.Vector(0.000000,0.000000,-60),App.Rotation(0.000000,0.000000,0.000000,1.000000))

sketch31.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),30),False)
sketch31.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 

sketch31.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),15),False)
sketch31.addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1)) 

sketch31.addGeometry(Part.Circle(App.Vector(8,-21,0),App.Vector(0,0,1),8),False)
sketch31.addSymmetric([2],-2,0) 

sketch31.trim(3,App.Vector(-4.671036,-13.775558,0))
sketch31.trim(2,App.Vector(4.397662,-13.864904,0))
sketch31.trim(3,App.Vector(-1.186513,-16.455961,0))
sketch31.trim(2,App.Vector(0.090503,-19.139975,0))
sketch31.trim(3,App.Vector(-11.270746,-28.304337,0))
sketch31.trim(2,App.Vector(10.701625,-28.702028,0))
sketch31.trim(0,App.Vector(-17.697254,-24.176645,0))
sketch31.trim(1,App.Vector(1.574561,15.313293,0))
sketch31.trim(1,App.Vector(0.207600,14.282619,0))

sketch32 = App.activeDocument().addObject('Sketcher::SketchObject','Sketch32')
sketch32.Placement = App.Placement(App.Vector(0.000000,0.000000,-75),App.Rotation(0.000000,0.000000,0.000000,1.000000))

sketch32.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),30),False)
sketch32.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 

sketch32.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),15),False)
sketch32.addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1)) 

sketch32.addGeometry(Part.Circle(App.Vector(8,-21,0),App.Vector(0,0,1),8),False)
sketch32.addSymmetric([2],-2,0) 

sketch32.trim(3,App.Vector(-4.671036,-13.775558,0))
sketch32.trim(2,App.Vector(4.397662,-13.864904,0))
sketch32.trim(3,App.Vector(-1.186513,-16.455961,0))
sketch32.trim(2,App.Vector(0.090503,-19.139975,0))
sketch32.trim(3,App.Vector(-11.270746,-28.304337,0))
sketch32.trim(2,App.Vector(10.701625,-28.702028,0))
sketch32.trim(0,App.Vector(-17.697254,-24.176645,0))
sketch32.trim(1,App.Vector(1.574561,15.313293,0))
sketch32.trim(1,App.Vector(0.207600,14.282619,0))

scale31 = Draft.scale([sketch31],delta=FreeCAD.Vector(2,2,2),center=FreeCAD.Vector(0,0,0),copy=False)   	#values
scale31.Label = 'Scale31'

scale32 = Draft.scale([sketch32],delta=FreeCAD.Vector(2,2,2),center=FreeCAD.Vector(0,0,0),copy=False)		#values
scale32.Label = 'Scale32'

loft31 = App.getDocument('Project').addObject('Part::Loft','Loft31')
loft31.Sections=[scale31, scale32, ]
loft31.Solid=True
loft31.Ruled=False
loft31.Closed=False

FreeCAD.ActiveDocument.recompute()

FreeCAD.ActiveDocument.recompute()

sketch41 = App.activeDocument().addObject('Sketcher::SketchObject','Sketch41')
sketch41.Placement = App.Placement(App.Vector(0.000000,0.000000,-80),App.Rotation(0.000000,0.000000,0.000000,1.000000))

sketch41.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),30),False)
sketch41.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 

sketch41.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),15),False)
sketch41.addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1)) 

sketch41.addGeometry(Part.Circle(App.Vector(8,-21,0),App.Vector(0,0,1),8),False)
sketch41.addSymmetric([2],-2,0) 

sketch41.trim(3,App.Vector(-4.671036,-13.775558,0))
sketch41.trim(2,App.Vector(4.397662,-13.864904,0))
sketch41.trim(3,App.Vector(-1.186513,-16.455961,0))
sketch41.trim(2,App.Vector(0.090503,-19.139975,0))
sketch41.trim(3,App.Vector(-11.270746,-28.304337,0))
sketch41.trim(2,App.Vector(10.701625,-28.702028,0))
sketch41.trim(0,App.Vector(-17.697254,-24.176645,0))
sketch41.trim(1,App.Vector(1.574561,15.313293,0))
sketch41.trim(1,App.Vector(0.207600,14.282619,0))

sketch42 = App.activeDocument().addObject('Sketcher::SketchObject','Sketch42')
sketch42.Placement = App.Placement(App.Vector(0.000000,0.000000,-95),App.Rotation(0.000000,0.000000,0.000000,1.000000))

sketch42.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),30),False)
sketch42.addConstraint(Sketcher.Constraint('Coincident',0,3,-1,1)) 

sketch42.addGeometry(Part.Circle(App.Vector(0.000000,0.000000,0),App.Vector(0,0,1),15),False)
sketch42.addConstraint(Sketcher.Constraint('Coincident',1,3,-1,1)) 

sketch42.addGeometry(Part.Circle(App.Vector(8,-21,0),App.Vector(0,0,1),8),False)
sketch42.addSymmetric([2],-2,0) 

sketch42.trim(3,App.Vector(-4.671036,-13.775558,0))
sketch42.trim(2,App.Vector(4.397662,-13.864904,0))
sketch42.trim(3,App.Vector(-1.186513,-16.455961,0))
sketch42.trim(2,App.Vector(0.090503,-19.139975,0))
sketch42.trim(3,App.Vector(-11.270746,-28.304337,0))
sketch42.trim(2,App.Vector(10.701625,-28.702028,0))
sketch42.trim(0,App.Vector(-17.697254,-24.176645,0))
sketch42.trim(1,App.Vector(1.574561,15.313293,0))
sketch42.trim(1,App.Vector(0.207600,14.282619,0))

scale41 = Draft.scale([sketch41],delta=FreeCAD.Vector(2,2,2),center=FreeCAD.Vector(0,0,0),copy=False)   	#values
scale41.Label = 'Scale41'

scale42 = Draft.scale([sketch42],delta=FreeCAD.Vector(2,2,2),center=FreeCAD.Vector(0,0,0),copy=False)		#values
scale42.Label = 'Scale42'

loft41 = App.getDocument('Project').addObject('Part::Loft','Loft41')
loft41.Sections=[scale41, scale42, ]
loft41.Solid=True
loft41.Ruled=False
loft41.Closed=False

FreeCAD.ActiveDocument.recompute()

FreeCAD.ActiveDocument.recompute()


Gui.SendMsgToActiveView("ViewFit")

Gui.activeDocument().activeView().viewAxonometric()


scale01.Placement.Base = App.Vector(353,376,487)
scale01.Placement.Rotation = App.Rotation(App.Vector(0,1,0),0.280859)
scale01.Placement.Rotation = App.Rotation(App.Vector(1,0,0),-1.06091)
scale01.Scale = (22.6669,23.1468,10)
scale02.Placement.Base = App.Vector(353,375,417)
scale02.Placement.Rotation = App.Rotation(App.Vector(0,1,0),-0.227363)
scale02.Placement.Rotation = App.Rotation(App.Vector(1,0,0),0)
scale02.Scale = (28.0002,23,10)
scale11.Placement.Base = App.Vector(353,375,392)
scale11.Placement.Rotation = App.Rotation(App.Vector(0,1,0),0.45653)
scale11.Placement.Rotation = App.Rotation(App.Vector(1,0,0),0.369645)
scale11.Scale = (27.8898,22.1433,9.57143)
scale12.Placement.Base = App.Vector(354,377,325)
scale12.Placement.Rotation = App.Rotation(App.Vector(0,1,0),0)
scale12.Placement.Rotation = App.Rotation(App.Vector(1,0,0),0.362627)
scale12.Scale = (29,22.5719,9.57143)
scale21.Placement.Base = App.Vector(354,376,298)
scale21.Placement.Rotation = App.Rotation(App.Vector(0,1,0),0)
scale21.Placement.Rotation = App.Rotation(App.Vector(1,0,0),0)
scale21.Scale = (29.3333,23.1468,9.42857)
scale22.Placement.Base = App.Vector(352,378,232)
scale22.Placement.Rotation = App.Rotation(App.Vector(0,1,0),-0.69306)
scale22.Placement.Rotation = App.Rotation(App.Vector(1,0,0),0)
scale22.Scale = (27.5576,22.2857,9.42857)
scale31.Placement.Base = App.Vector(353,375,206)
scale31.Placement.Rotation = App.Rotation(App.Vector(0,1,0),-0.229182)
scale31.Placement.Rotation = App.Rotation(App.Vector(1,0,0),0.369645)
scale31.Scale = (27.778,22.1433,9.42857)
scale32.Placement.Base = App.Vector(353,376,140)
scale32.Placement.Rotation = App.Rotation(App.Vector(0,1,0),0)
scale32.Placement.Rotation = App.Rotation(App.Vector(1,0,0),0)
scale32.Scale = (25.3333,22.5714,9.42857)
scale41.Placement.Base = App.Vector(353,376,114)
scale41.Placement.Rotation = App.Rotation(App.Vector(0,1,0),-0.244852)
scale41.Placement.Rotation = App.Rotation(App.Vector(1,0,0),-0.720664)
scale41.Scale = (26.0002,22.7161,9.57143)
scale42.Placement.Base = App.Vector(354,374,47)
scale42.Placement.Rotation = App.Rotation(App.Vector(0,1,0),-0.280859)
scale42.Placement.Rotation = App.Rotation(App.Vector(1,0,0),-0.358094)
scale42.Scale = (22.6669,22.8576,9.57143)
FreeCAD.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxonometric()
volume01 = loft01.Shape.Volume
volume02 = loft11.Shape.Volume
volume03 = loft21.Shape.Volume
volume04 = loft31.Shape.Volume
volume05 = loft41.Shape.Volume
totalvolume = loft01.Shape.Volume + loft11.Shape.Volume + loft21.Shape.Volume + loft31.Shape.Volume + loft41.Shape.Volume
volume01
volume02
volume03
volume04
volume05
totalvolume
