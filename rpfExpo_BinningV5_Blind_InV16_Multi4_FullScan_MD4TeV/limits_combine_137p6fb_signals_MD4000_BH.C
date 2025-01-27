void limits_combine_137p6fb_signals_MD4000_BH()
{
//=========Macro generated from canvas: climits/climits
//=========  (Sun Jan 26 12:00:04 2025) by ROOT version 6.14/09
   TCanvas *climits = new TCanvas("climits", "climits",0,0,700,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   climits->SetHighLightColor(2);
   climits->Range(3.149,-6,11.969,0.6666667);
   climits->SetFillColor(0);
   climits->SetBorderMode(0);
   climits->SetBorderSize(2);
   climits->SetLogy();
   climits->SetTickx(1);
   climits->SetTicky(1);
   climits->SetLeftMargin(0.15);
   climits->SetRightMargin(0.05);
   climits->SetBottomMargin(0.15);
   climits->SetFrameFillStyle(0);
   climits->SetFrameBorderMode(0);
   climits->SetFrameFillStyle(0);
   climits->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1[7] = {
   5,
   6,
   7,
   8,
   9,
   10,
   11};
   Double_t Graph0_fy1[7] = {
   0.001464687,
   0.0003777949,
   0.0001073931,
   4.405373e-05,
   2.783095e-05,
   2.174325e-05,
   1.887145e-05};
   TGraph *graph = new TGraph(7,Graph0_fx1,Graph0_fy1);
   graph->SetName("Graph0");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineStyle(2);
   graph->SetLineWidth(3);
   graph->SetMarkerStyle(21);
   graph->SetMarkerSize(0);
   
   TH1F *Graph_Graph01 = new TH1F("Graph_Graph01","",100,4.4,11.6);
   Graph_Graph01->SetMinimum(1e-05);
   Graph_Graph01->SetMaximum(1);
   Graph_Graph01->SetDirectory(0);
   Graph_Graph01->SetStats(0);
   Graph_Graph01->SetLineStyle(0);
   Graph_Graph01->SetMarkerStyle(20);
   Graph_Graph01->GetXaxis()->SetTitle("m(BH) [TeV]");
   Graph_Graph01->GetXaxis()->SetRange(2,99);
   Graph_Graph01->GetXaxis()->SetLabelFont(42);
   Graph_Graph01->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph01->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph01->GetXaxis()->SetTitleSize(0.055);
   Graph_Graph01->GetXaxis()->SetTitleOffset(1.25);
   Graph_Graph01->GetXaxis()->SetTitleFont(42);
   Graph_Graph01->GetYaxis()->SetTitle("Cross Section [pb]");
   Graph_Graph01->GetYaxis()->SetLabelFont(42);
   Graph_Graph01->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph01->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph01->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph01->GetYaxis()->SetTitleOffset(1.5);
   Graph_Graph01->GetYaxis()->SetTitleFont(42);
   Graph_Graph01->GetZaxis()->SetLabelFont(42);
   Graph_Graph01->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph01->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph01->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph01->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph01);
   
   graph->Draw("al");
   
   Double_t Graph1_fx2[16] = {
   5,
   6,
   7,
   8,
   9,
   10,
   11,
   11,
   11,
   11,
   10,
   9,
   8,
   7,
   6,
   5};
   Double_t Graph1_fy2[16] = {
   0.00337598,
   0.0009061741,
   0.0003137321,
   0.0001339489,
   8.46289e-05,
   6.611786e-05,
   5.738515e-05,
   5.738515e-05,
   5.528744e-06,
   5.528744e-06,
   6.370093e-06,
   8.262313e-06,
   1.307845e-05,
   3.356035e-05,
   0.0001269155,
   0.0004920433};
   graph = new TGraph(16,Graph1_fx2,Graph1_fy2);
   graph->SetName("Graph1");
   graph->SetTitle("Graph");

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#ffcc00");
   graph->SetFillColor(ci);
   graph->SetFillStyle(1000);
   graph->SetLineColor(0);
   graph->SetMarkerStyle(20);
   
   TH1F *Graph_Graph12 = new TH1F("Graph_Graph12","Graph",100,4.4,11.6);
   Graph_Graph12->SetMinimum(4.97587e-06);
   Graph_Graph12->SetMaximum(0.003713025);
   Graph_Graph12->SetDirectory(0);
   Graph_Graph12->SetStats(0);
   Graph_Graph12->SetLineStyle(0);
   Graph_Graph12->SetMarkerStyle(20);
   Graph_Graph12->GetXaxis()->SetLabelFont(42);
   Graph_Graph12->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph12->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph12->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph12->GetXaxis()->SetTitleFont(42);
   Graph_Graph12->GetYaxis()->SetLabelFont(42);
   Graph_Graph12->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph12->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph12->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph12->GetYaxis()->SetTitleFont(42);
   Graph_Graph12->GetZaxis()->SetLabelFont(42);
   Graph_Graph12->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph12->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph12->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph12);
   
   graph->Draw("lf");
   
   Double_t Graph2_fx3[16] = {
   5,
   6,
   7,
   8,
   9,
   10,
   11,
   11,
   11,
   11,
   10,
   9,
   8,
   7,
   6,
   5};
   Double_t Graph2_fy3[16] = {
   0.002439684,
   0.0006458463,
   0.0001977166,
   8.444174e-05,
   5.356795e-05,
   4.202392e-05,
   3.654871e-05,
   3.654871e-05,
   9.802578e-06,
   9.802578e-06,
   1.129431e-05,
   1.453039e-05,
   2.300022e-05,
   5.778672e-05,
   0.0002092353,
   0.0007959945};
   graph = new TGraph(16,Graph2_fx3,Graph2_fy3);
   graph->SetName("Graph2");
   graph->SetTitle("Graph");

   ci = TColor::GetColor("#00cc00");
   graph->SetFillColor(ci);
   graph->SetFillStyle(1000);
   graph->SetLineColor(0);
   graph->SetMarkerStyle(20);
   
   TH1F *Graph_Graph23 = new TH1F("Graph_Graph23","Graph",100,4.4,11.6);
   Graph_Graph23->SetMinimum(8.82232e-06);
   Graph_Graph23->SetMaximum(0.002682672);
   Graph_Graph23->SetDirectory(0);
   Graph_Graph23->SetStats(0);
   Graph_Graph23->SetLineStyle(0);
   Graph_Graph23->SetMarkerStyle(20);
   Graph_Graph23->GetXaxis()->SetLabelFont(42);
   Graph_Graph23->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph23->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph23->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph23->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph23->GetXaxis()->SetTitleFont(42);
   Graph_Graph23->GetYaxis()->SetLabelFont(42);
   Graph_Graph23->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph23->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph23->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph23->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph23->GetYaxis()->SetTitleFont(42);
   Graph_Graph23->GetZaxis()->SetLabelFont(42);
   Graph_Graph23->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph23->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph23->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph23->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph23);
   
   graph->Draw("lf");
   
   Double_t Graph0_fx4[7] = {
   5,
   6,
   7,
   8,
   9,
   10,
   11};
   Double_t Graph0_fy4[7] = {
   0.001464687,
   0.0003777949,
   0.0001073931,
   4.405373e-05,
   2.783095e-05,
   2.174325e-05,
   1.887145e-05};
   graph = new TGraph(7,Graph0_fx4,Graph0_fy4);
   graph->SetName("Graph0");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineStyle(2);
   graph->SetLineWidth(3);
   graph->SetMarkerStyle(21);
   graph->SetMarkerSize(0);
   
   TH1F *Graph_Graph_Graph014 = new TH1F("Graph_Graph_Graph014","",100,4.4,11.6);
   Graph_Graph_Graph014->SetMinimum(1e-05);
   Graph_Graph_Graph014->SetMaximum(1);
   Graph_Graph_Graph014->SetDirectory(0);
   Graph_Graph_Graph014->SetStats(0);
   Graph_Graph_Graph014->SetLineStyle(0);
   Graph_Graph_Graph014->SetMarkerStyle(20);
   Graph_Graph_Graph014->GetXaxis()->SetTitle("m(BH) [TeV]");
   Graph_Graph_Graph014->GetXaxis()->SetRange(2,99);
   Graph_Graph_Graph014->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph014->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph014->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph014->GetXaxis()->SetTitleSize(0.055);
   Graph_Graph_Graph014->GetXaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph014->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph014->GetYaxis()->SetTitle("Cross Section [pb]");
   Graph_Graph_Graph014->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph014->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph014->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph014->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph_Graph014->GetYaxis()->SetTitleOffset(1.5);
   Graph_Graph_Graph014->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph014->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph014->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph014->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph014->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph_Graph014->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph014);
   
   graph->Draw("l");
   
   Double_t _fx5[7] = {
   5,
   6,
   7,
   8,
   9,
   10,
   11};
   Double_t _fy5[7] = {
   0.675984,
   0.135296,
   0.0218575,
   0.00263422,
   0.000205028,
   8.23413e-06,
   1.24564e-07};
   graph = new TGraph(7,_fx5,_fy5);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(3);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(0.5);
   
   TH1F *Graph_Graph5 = new TH1F("Graph_Graph5","",100,4.4,11.6);
   Graph_Graph5->SetMinimum(0.0003);
   Graph_Graph5->SetMaximum(100);
   Graph_Graph5->SetDirectory(0);
   Graph_Graph5->SetStats(0);
   Graph_Graph5->SetLineStyle(0);
   Graph_Graph5->SetMarkerStyle(20);
   Graph_Graph5->GetXaxis()->SetLabelFont(42);
   Graph_Graph5->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph5->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph5->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph5->GetXaxis()->SetTitleFont(42);
   Graph_Graph5->GetYaxis()->SetLabelFont(42);
   Graph_Graph5->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph5->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph5->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph5->GetYaxis()->SetTitleFont(42);
   Graph_Graph5->GetZaxis()->SetLabelFont(42);
   Graph_Graph5->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph5->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph5->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph5);
   
   graph->Draw("l");
   
   Double_t _fx6[7] = {
   5,
   6,
   7,
   8,
   9,
   10,
   11};
   Double_t _fy6[7] = {
   0.6083856,
   0.1217664,
   0.01967175,
   0.002370798,
   0.0001845252,
   7.410717e-06,
   1.121076e-07};
   graph = new TGraph(7,_fx6,_fy6);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineStyle(2);
   graph->SetLineWidth(2);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(0.5);
   
   TH1F *Graph_Graph6 = new TH1F("Graph_Graph6","",100,4.4,11.6);
   Graph_Graph6->SetMinimum(1.008968e-07);
   Graph_Graph6->SetMaximum(0.6692241);
   Graph_Graph6->SetDirectory(0);
   Graph_Graph6->SetStats(0);
   Graph_Graph6->SetLineStyle(0);
   Graph_Graph6->SetMarkerStyle(20);
   Graph_Graph6->GetXaxis()->SetLabelFont(42);
   Graph_Graph6->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph6->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph6->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph6->GetXaxis()->SetTitleFont(42);
   Graph_Graph6->GetYaxis()->SetLabelFont(42);
   Graph_Graph6->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph6->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph6->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph6->GetYaxis()->SetTitleFont(42);
   Graph_Graph6->GetZaxis()->SetLabelFont(42);
   Graph_Graph6->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph6->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph6->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph6);
   
   graph->Draw("l");
   
   Double_t _fx7[7] = {
   5,
   6,
   7,
   8,
   9,
   10,
   11};
   Double_t _fy7[7] = {
   0.7435824,
   0.1488256,
   0.02404325,
   0.002897642,
   0.0002255308,
   9.057543e-06,
   1.370204e-07};
   graph = new TGraph(7,_fx7,_fy7);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineStyle(2);
   graph->SetLineWidth(2);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(0.5);
   
   TH1F *Graph_Graph7 = new TH1F("Graph_Graph7","",100,4.4,11.6);
   Graph_Graph7->SetMinimum(1.233184e-07);
   Graph_Graph7->SetMaximum(0.8179406);
   Graph_Graph7->SetDirectory(0);
   Graph_Graph7->SetStats(0);
   Graph_Graph7->SetLineStyle(0);
   Graph_Graph7->SetMarkerStyle(20);
   Graph_Graph7->GetXaxis()->SetLabelFont(42);
   Graph_Graph7->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph7->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph7->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph7->GetXaxis()->SetTitleFont(42);
   Graph_Graph7->GetYaxis()->SetLabelFont(42);
   Graph_Graph7->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph7->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph7->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph7->GetYaxis()->SetTitleFont(42);
   Graph_Graph7->GetZaxis()->SetLabelFont(42);
   Graph_Graph7->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph7->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph7->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph7);
   
   graph->Draw("l");
   
   TLegend *leg = new TLegend(0.5,0.6,0.92,0.89,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextFont(62);
   leg->SetLineColor(0);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("NULL","95% CL Upper Limits","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph1","Expected Limit #pm1#sigma, #pm2#sigma","f");

   ci = TColor::GetColor("#ffcc00");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1000);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("","#sigma^{NNLO+NNLL}_{th}(BH)#pm1#sigma","l");
   entry->SetLineColor(4);
   entry->SetLineStyle(1);
   entry->SetLineWidth(3);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   leg->Draw();
   TLine *line = new TLine(0.517,0.75,0.588,0.75);

   ci = TColor::GetColor("#00cc00");
   line->SetLineColor(ci);
   line->SetLineWidth(22);
   line->Draw();
   line = new TLine(0.517,0.75,0.588,0.75);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   line = new TLine(0.517,0.66,0.588,0.66);
   line->SetLineColor(4);
   line->SetLineStyle(2);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.517,0.64,0.588,0.64);
   line->SetLineColor(4);
   line->SetLineStyle(2);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(9.67284,0,9.67284,2.357204e-05);

   ci = TColor::GetColor("#666666");
   line->SetLineColor(ci);
   line->SetLineStyle(2);
   line->Draw();
   TLatex *   tex = new TLatex(9.66784,0,"  9.67 TeV");

   ci = TColor::GetColor("#666666");
   tex->SetTextColor(ci);
   tex->SetTextFont(43);
   tex->SetTextSize(14);
   tex->SetTextAngle(90);
   tex->SetLineWidth(2);
   tex->Draw();
   
   TH1F *Graph_copy = new TH1F("Graph_copy","",100,4.4,11.6);
   Graph_copy->SetMinimum(1e-05);
   Graph_copy->SetMaximum(1);
   Graph_copy->SetDirectory(0);
   Graph_copy->SetStats(0);
   Graph_copy->SetLineStyle(0);
   Graph_copy->SetMarkerStyle(20);
   Graph_copy->GetXaxis()->SetTitle("m(BH) [TeV]");
   Graph_copy->GetXaxis()->SetRange(2,99);
   Graph_copy->GetXaxis()->SetLabelFont(42);
   Graph_copy->GetXaxis()->SetLabelOffset(0.007);
   Graph_copy->GetXaxis()->SetLabelSize(0.05);
   Graph_copy->GetXaxis()->SetTitleSize(0.055);
   Graph_copy->GetXaxis()->SetTitleOffset(1.25);
   Graph_copy->GetXaxis()->SetTitleFont(42);
   Graph_copy->GetYaxis()->SetTitle("Cross Section [pb]");
   Graph_copy->GetYaxis()->SetLabelFont(42);
   Graph_copy->GetYaxis()->SetLabelOffset(0.007);
   Graph_copy->GetYaxis()->SetLabelSize(0.05);
   Graph_copy->GetYaxis()->SetTitleSize(0.05);
   Graph_copy->GetYaxis()->SetTitleOffset(1.5);
   Graph_copy->GetYaxis()->SetTitleFont(42);
   Graph_copy->GetZaxis()->SetLabelFont(42);
   Graph_copy->GetZaxis()->SetLabelOffset(0.007);
   Graph_copy->GetZaxis()->SetLabelSize(0.05);
   Graph_copy->GetZaxis()->SetTitleSize(0.06);
   Graph_copy->GetZaxis()->SetTitleFont(42);
   Graph_copy->Draw("sameaxis");
      tex = new TLatex(0.95,0.915,"35.9 fb^{-1} + 41.5 fb^{-1} + 60 fb^{-1} (13 TeV)");
tex->SetNDC();
   tex->SetTextAlign(31);
   tex->SetTextFont(42);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.15,0.915,"CMS");
tex->SetNDC();
   tex->SetTextFont(61);
   tex->SetTextSize(0.08);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.3,0.96,"");
tex->SetNDC();
   tex->SetTextAlign(13);
   tex->SetTextFont(52);
   tex->SetTextSize(0.0608);
   tex->SetLineWidth(2);
   tex->Draw();
   climits->Modified();
   climits->cd();
   climits->SetSelected(climits);
}
