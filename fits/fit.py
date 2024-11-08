import os
import sys

from ROOT import RooRealVar, RooDataSet, RooGaussian, RooConstVar, RooChebychev, RooAddPdf, RooSimultaneous, RooCategory, TCanvas, TAxis, RooPlot, TFile, gROOT, RooDataHist, RooArgList, RooFormulaVar, RooGenericPdf, RooFFTConvPdf, gPad

gROOT.SetBatch(True)

index = sys.argv[1]

rho = RooRealVar("rho","rho",0.8,1.3,"cm");


f = TFile("/home/belle/varghese/DESY/BASF2/Physics_Analysis/B2BII/hadronic_vertices/fits/Saved_Hists.root");

h1 = f.Get("h%s_phislices"%index);


Data = RooDataHist("Data", "Data", RooArgList(rho), h1, 1.0) ; 


#PDF modelling

p = RooRealVar("p","p",-0.6,-1.0,1.0); 



shift1 = RooRealVar("shift1","shift1",0.02,-0.08, 0.08);
shift2 = RooRealVar("shift2","shift2",0.02,-0.08, 0.08);
Edge1 = RooFormulaVar("Edge1","1.0+shift1",RooArgList(shift1));
Edge2 = RooFormulaVar("Edge2","1.06+shift1",RooArgList(shift1));
Edge3 = RooFormulaVar("Edge3","1.16+shift1",RooArgList(shift1));
Edge4 = RooFormulaVar("Edge4","1.20+shift1",RooArgList(shift1));



step1 = RooGenericPdf("step1", "step1", "((@0 >= 0.8) && (@0 < @1))*(1.5+(@0*@2))", RooArgList(rho, Edge1, p));
step2 = RooGenericPdf("step2", "step2", "((@0 >= @1) && (@0 < @2))*(1.5+(@0*@3))", RooArgList(rho, Edge1, Edge2, p));
step3 = RooGenericPdf("step3", "step3", "((@0 >= @1) && (@0 < @2))*(1.5+(@0*@3))", RooArgList(rho, Edge2, Edge3, p));
step4 = RooGenericPdf("step4", "step4", "((@0 >= @1) && (@0 < @2))*(1.5+(@0*@3))", RooArgList(rho, Edge3, Edge4, p));
step5 = RooGenericPdf("step5", "step5", "((@0 >= @1) && (@0 < 1.3))*(1.5+(@0*@2))", RooArgList(rho, Edge4, p));



f1 = RooRealVar("f1","f1",1000,0,5000);
f2 = RooRealVar("f2","f2",3600,0,5000);
f3 = RooRealVar("f3","f3",1850,0,5000);
f4 = RooRealVar("f4","f4",3600,0,5000);
f5 = RooRealVar("f5","f5",1850,0,5000);



model = RooAddPdf("model","model",RooArgList(step1,step2,step3,step4,step5),RooArgList(f1,f2,f3,f4,f5));


# Construct triple gaussian
mg = RooRealVar("mg","mg",0) ;
sg1 = RooRealVar("sg1","sg1",0.001235);
sg2 = RooRealVar("sg2","sg2",0.00364);
sg3 = RooRealVar("sg3","sg3",0.0126);

gauss = RooGaussian("gauss","gauss",rho,mg,sg1) ;
gauss2 = RooGaussian("gauss2","gauss2",rho,mg,sg2) ;
gauss3 = RooGaussian("gauss3","gauss3",rho,mg,sg3) ;

F1 = RooRealVar("F1","F1",0.41);
F2 = RooRealVar("F2","F2",0.36);

comGaus = RooAddPdf("comGaus","comGaus",RooArgList(gauss,gauss2,gauss3),RooArgList(F1,F2));


Model = RooFFTConvPdf("Model","Model",rho,model,comGaus); 


#fitRes = model.fitTo(Data)
fitRes = Model.fitTo(Data);




#PLOTING
#frame =rho.frame(title="Rho projection", nBins=100);
frame =rho.frame()
Data.plotOn(frame);
Model.plotOn(frame);
#model.plotOn(frame);

can3 = TCanvas("c3","c3",1200,600) ;
gPad.SetLeftMargin(0.15) ; gPad.SetBottomMargin(0.15); frame.Draw() ;

can3.SaveAs("plots/fit_%s.png"%index);
can3.Close();


phi = 2.5+(5.0*float(index))

outfile = open("/home/belle/varghese/DESY/BASF2/Physics_Analysis/B2BII/hadronic_vertices/fits/result.txt", "a")  
outfile.write("%s\t%s\t%s\n" %(phi,shift1.getVal(), shift1.getError())) 
outfile.close()




















