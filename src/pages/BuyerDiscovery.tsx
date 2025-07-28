import { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { Textarea } from "@/components/ui/textarea";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Separator } from "@/components/ui/separator";
import { Label } from "@/components/ui/label";
import { Search, Filter, Download, Building2, MapPin, Users, TrendingUp, Star, Phone, Mail, Calendar, Globe, Target, BarChart3, ExternalLink, Loader2, CheckCircle, AlertCircle, Play, Eye, MessageCircle } from "lucide-react";

// Mock research result based on your example
const mockResearchResult = {
  sourceCompany: {
    name: "Viyash Life Sciences",
    url: "https://www.viyash.com/",
    overview: "Viyash Life Sciences is a privately held, India-headquartered pharmaceutical enterprise that has rapidly scaled via acquisitions and organic growth. It operates 10 API/intermediate plants (≈2,000 KL combined capacity) plus one US FDA-approved oral solid dosage (OSD) facility in New Jersey.",
    businessModel: "Integrated developer–manufacturer of niche active pharmaceutical ingredients (APIs), advanced intermediates, and select finished dosage forms; also provides contract development & manufacturing (CDMO) services.",
    therapeuticCoverage: "Diversified API pipeline (>75 commercial, 25+ pipeline) spanning anti-infective, cardiovascular (CV), CNS, diabetes, oncology, ARV, analgesics, antihistamines, anticoagulants, GI, urology, etc."
  },
  idealCustomerProfile: "Mid-size to upper-mid generic formulation companies, specialty pharma, and regional CDMOs seeking reliable, compliant API supply or co-development partners.",
  discoveredBuyers: [
    {
      id: 1,
      name: "Amneal Pharmaceuticals LLC",
      website: "https://amneal.com",
      country: "United States",
      region: "Global",
      targetSegment: "Large US-based generics & specialty pharma (≈270 products)",
      keyContacts: [
        { name: "Chirag Patel", role: "President & Co-CEO" },
        { name: "Chintu Patel", role: "Co-CEO" },
        { name: "Business Development", email: "BusinessDevelopment@amneal.com" }
      ],
      reasonForRecommendation: "Consolidating API vendors to cut costs and speed development; complex oral solids, injectables, biosimilars pipeline aligns to Viyash's oncology/CV/CNS APIs and high-potency capabilities; US FDA compliance on both sides eases tech transfer.",
      opportunityScore: 92,
      status: "High Priority"
    },
    {
      id: 2,
      name: "Apotex Inc.",
      website: "https://www.apotex.com",
      country: "Canada",
      region: "Americas / 70+ countries",
      targetSegment: "Tier-1 generic manufacturer & API trader",
      keyContacts: [
        { name: "Allan Oberman", role: "President & CEO" }
      ],
      reasonForRecommendation: "Global API sourcing for 485+ generic medicines; pursuing growth in Americas after EU divestiture; needs compliant API partners to support high-volume launches; Viyash's DMF portfolio covers Apotex's molecules (e.g., abacavir, apixaban).",
      opportunityScore: 88,
      status: "High Priority"
    },
    {
      id: 3,
      name: "Nichi-Iko Pharmaceutical Co. Ltd.",
      website: "https://www.nichiiko.co.jp",
      country: "Japan",
      region: "Asia Global",
      targetSegment: "Japan's top generic player with 11 Bn-tablet capacity; expanding overseas manufacturing",
      keyContacts: [
        { name: "Shingo Iwamoto", role: "CEO & President" }
      ],
      reasonForRecommendation: "Reorganizing supply chain, seeking external API capacity post-restructuring; focuses on 'high-quality generics' for Japan & China, requiring USFDA/EU-GMP sites; Viyash offers cost-effective, quality-audited oncology & CV APIs matching Nichi-Iko portfolio.",
      opportunityScore: 85,
      status: "Medium Priority"
    },
    {
      id: 4,
      name: "Laboratorios Farmacéuticos ROVI S.A.",
      website: "https://roviservices.com",
      country: "Spain",
      region: "EU / 80+ export markets",
      targetSegment: "High-value injectable CDMO and branded LMWH producer",
      keyContacts: [
        { name: "Juan López-Belmonte Encina", role: "Chairman & CEO" },
        { name: "Rafael Crespo Mora", role: "BD, Contract Mfg." }
      ],
      reasonForRecommendation: "CDMO sales forecast to double to €700 M by 2030 with extra fill-finish lines; requires large-scale API sources (oncology, LMWH precursors); Viyash's sterile/HPAPI capability and Grignard expertise suit ROVI's injectable projects; both hold USFDA approvals facilitating supply.",
      opportunityScore: 82,
      status: "Medium Priority"
    },
    {
      id: 5,
      name: "Rameda",
      website: "https://ramedapharma.com",
      country: "Egypt",
      region: "MENA & Africa (exports to 10+ countries)",
      targetSegment: "Branded generic manufacturer, toll mfg., export-oriented",
      keyContacts: [
        { name: "Dr. Amr Morsy", role: "CEO" },
        { name: "Khaled Daader", role: "Head M&A & IR" }
      ],
      reasonForRecommendation: "Monetizes spare OSD & injectable capacity via toll manufacturing; sources APIs for 129 products across 12 therapeutic areas; Viyash's ARV, CV, GI and antihistamine APIs match Rameda's domestic tender portfolio; Egypt demands cost-efficient quality APIs for government tenders.",
      opportunityScore: 78,
      status: "Medium Priority"
    }
  ]
};

const BuyerDiscovery = () => {
  const [companyUrl, setCompanyUrl] = useState("");
  const [isResearching, setIsResearching] = useState(false);
  const [hasResults, setHasResults] = useState(false);
  const [activeUIOption, setActiveUIOption] = useState("cards"); // cards, table, detailed

  const handleResearch = async () => {
    setIsResearching(true);
    // Simulate API call
    setTimeout(() => {
      setIsResearching(false);
      setHasResults(true);
    }, 3000);
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case "High Priority":
        return "bg-gradient-primary";
      case "Medium Priority":
        return "bg-yellow-500";
      case "Low Priority":
        return "bg-gray-500";
      default:
        return "bg-gray-500";
    }
  };

  const getOpportunityScoreColor = (score: number) => {
    if (score >= 90) return "text-green-600";
    if (score >= 80) return "text-yellow-600";
    return "text-gray-600";
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-gradient-card shadow-card">
        <div className="flex h-16 items-center justify-between px-6">
          <div className="flex items-center gap-6">
            <h1 className="text-xl font-bold text-foreground">AI-Powered Buyer Discovery Engine</h1>
          </div>
          <div className="flex items-center gap-3">
            {hasResults && (
              <>
                <Button variant="outline" size="sm" className="gap-2">
                  <Download className="w-4 h-4" />
                  Export Report
                </Button>
                <Button variant="outline" size="sm" className="gap-2">
                  <MessageCircle className="w-4 h-4" />
                  Generate Outreach
                </Button>
              </>
            )}
          </div>
        </div>
      </header>

      <main className="p-6 space-y-6">
        {/* Research Input Form */}
        <Card className="bg-gradient-card border-border">
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-foreground">
              <Target className="w-5 h-5" />
              Company Research & Buyer Discovery
            </CardTitle>
            <p className="text-sm text-muted-foreground">
              Enter your company's website URL to discover potential buyers and partners using AI-powered market research.
            </p>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="company-url">Source Company Website URL</Label>
              <div className="flex gap-2">
                <Input
                  id="company-url"
                  placeholder="https://www.yourcompany.com"
                  value={companyUrl}
                  onChange={(e) => setCompanyUrl(e.target.value)}
                  className="flex-1"
                />
                <Button 
                  onClick={handleResearch}
                  disabled={!companyUrl || isResearching}
                  className="gap-2 min-w-[140px]"
                >
                  {isResearching ? (
                    <>
                      <Loader2 className="w-4 h-4 animate-spin" />
                      Researching...
                    </>
                  ) : (
                    <>
                      <Play className="w-4 h-4" />
                      Start Research
                    </>
                  )}
                </Button>
              </div>
            </div>
            
            {isResearching && (
              <div className="bg-muted/20 rounded-lg p-4 space-y-2">
                <div className="flex items-center gap-2">
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span className="text-sm font-medium">AI Research in Progress...</span>
                </div>
                <div className="text-xs text-muted-foreground space-y-1">
                  <div>• Analyzing company website and business model</div>
                  <div>• Identifying product portfolio and capabilities</div>
                  <div>• Defining ideal customer profile</div>
                  <div>• Searching for real target companies</div>
                  <div>• Generating evidence-backed recommendations</div>
                </div>
              </div>
            )}
          </CardContent>
        </Card>

        {/* Results Section */}
        {hasResults && (
          <>
            {/* Source Company Overview */}
            <Card className="bg-gradient-card border-border">
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-foreground">
                  <Building2 className="w-5 h-5" />
                  Source Company Analysis
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div>
                  <h3 className="font-semibold text-foreground mb-2">{mockResearchResult.sourceCompany.name}</h3>
                  <p className="text-sm text-muted-foreground mb-3">{mockResearchResult.sourceCompany.overview}</p>
                  
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <h4 className="font-medium text-foreground mb-1">Business Model</h4>
                      <p className="text-sm text-muted-foreground">{mockResearchResult.sourceCompany.businessModel}</p>
                    </div>
                    <div>
                      <h4 className="font-medium text-foreground mb-1">Therapeutic Coverage</h4>
                      <p className="text-sm text-muted-foreground">{mockResearchResult.sourceCompany.therapeuticCoverage}</p>
                    </div>
                  </div>
                </div>

                <Separator />
                
                <div>
                  <h4 className="font-medium text-foreground mb-2">Ideal Customer Profile</h4>
                  <p className="text-sm text-muted-foreground">{mockResearchResult.idealCustomerProfile}</p>
                </div>
              </CardContent>
            </Card>

            {/* Stats Cards */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              <Card className="bg-gradient-card border-border">
                <CardContent className="p-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-gradient-primary rounded-lg flex items-center justify-center">
                      <Target className="w-5 h-5 text-primary-foreground" />
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Targets Found</p>
                      <p className="text-2xl font-bold text-foreground">{mockResearchResult.discoveredBuyers.length}</p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-card border-border">
                <CardContent className="p-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-gradient-success rounded-lg flex items-center justify-center">
                      <TrendingUp className="w-5 h-5 text-success-foreground" />
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">High Priority</p>
                      <p className="text-2xl font-bold text-foreground">
                        {mockResearchResult.discoveredBuyers.filter(b => b.status === "High Priority").length}
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-card border-border">
                <CardContent className="p-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-accent/20 rounded-lg flex items-center justify-center">
                      <BarChart3 className="w-5 h-5 text-accent" />
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Avg. Score</p>
                      <p className="text-2xl font-bold text-foreground">
                        {Math.round(mockResearchResult.discoveredBuyers.reduce((acc, b) => acc + b.opportunityScore, 0) / mockResearchResult.discoveredBuyers.length)}
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-card border-border">
                <CardContent className="p-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-primary/20 rounded-lg flex items-center justify-center">
                      <Globe className="w-5 h-5 text-primary" />
                    </div>
                    <div>
                      <p className="text-sm text-muted-foreground">Regions</p>
                      <p className="text-2xl font-bold text-foreground">
                        {new Set(mockResearchResult.discoveredBuyers.map(b => b.country)).size}
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* UI Options Tabs */}
            <Card className="bg-gradient-card border-border">
              <CardHeader>
                <div className="flex items-center justify-between">
                  <CardTitle className="text-foreground">Discovered Buyers</CardTitle>
                  <Tabs value={activeUIOption} onValueChange={setActiveUIOption} className="w-auto">
                    <TabsList className="grid w-full grid-cols-3">
                      <TabsTrigger value="cards">Cards View</TabsTrigger>
                      <TabsTrigger value="table">Table View</TabsTrigger>
                      <TabsTrigger value="detailed">Detailed View</TabsTrigger>
                    </TabsList>
                  </Tabs>
                </div>
              </CardHeader>
              <CardContent>
                <Tabs value={activeUIOption} className="w-full">
                  {/* Cards View */}
                  <TabsContent value="cards" className="space-y-4 mt-0">
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                      {mockResearchResult.discoveredBuyers.map((buyer) => (
                        <Card key={buyer.id} className="border-border hover:shadow-md transition-shadow">
                          <CardHeader className="pb-3">
                            <div className="flex items-start justify-between">
                              <div>
                                <h3 className="font-semibold text-foreground text-sm">{buyer.name}</h3>
                                <p className="text-xs text-muted-foreground">{buyer.country}</p>
                              </div>
                              <div className="flex items-center gap-1">
                                <Star className={`w-4 h-4 ${getOpportunityScoreColor(buyer.opportunityScore)}`} />
                                <span className={`text-sm font-medium ${getOpportunityScoreColor(buyer.opportunityScore)}`}>
                                  {buyer.opportunityScore}
                                </span>
                              </div>
                            </div>
                            <Badge className={`${getStatusColor(buyer.status)} text-white w-fit`}>
                              {buyer.status}
                            </Badge>
                          </CardHeader>
                          <CardContent className="pt-0 space-y-3">
                            <p className="text-xs text-muted-foreground">{buyer.targetSegment}</p>
                            <div className="space-y-1">
                              <h4 className="text-xs font-medium text-foreground">Key Contacts:</h4>
                              {buyer.keyContacts.slice(0, 2).map((contact, idx) => (
                                <p key={idx} className="text-xs text-muted-foreground">
                                  {contact.name} - {contact.role}
                                </p>
                              ))}
                            </div>
                            <div className="flex gap-2">
                              <Button size="sm" variant="outline" className="flex-1 text-xs">
                                <Eye className="w-3 h-3 mr-1" />
                                View
                              </Button>
                              <Button size="sm" className="flex-1 text-xs">
                                <ExternalLink className="w-3 h-3 mr-1" />
                                Visit
                              </Button>
                            </div>
                          </CardContent>
                        </Card>
                      ))}
                    </div>
                  </TabsContent>

                  {/* Table View */}
                  <TabsContent value="table" className="mt-0">
                    <Table>
                      <TableHeader>
                        <TableRow>
                          <TableHead>Company</TableHead>
                          <TableHead>Country/Region</TableHead>
                          <TableHead>Segment</TableHead>
                          <TableHead>Score</TableHead>
                          <TableHead>Status</TableHead>
                          <TableHead>Actions</TableHead>
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        {mockResearchResult.discoveredBuyers.map((buyer) => (
                          <TableRow key={buyer.id}>
                            <TableCell>
                              <div>
                                <div className="font-medium">{buyer.name}</div>
                                <div className="text-sm text-muted-foreground">{buyer.website}</div>
                              </div>
                            </TableCell>
                            <TableCell>{buyer.country}</TableCell>
                            <TableCell className="max-w-[200px]">
                              <div className="truncate" title={buyer.targetSegment}>
                                {buyer.targetSegment}
                              </div>
                            </TableCell>
                            <TableCell>
                              <div className="flex items-center gap-1">
                                <Star className={`w-4 h-4 ${getOpportunityScoreColor(buyer.opportunityScore)}`} />
                                <span className={`font-medium ${getOpportunityScoreColor(buyer.opportunityScore)}`}>
                                  {buyer.opportunityScore}
                                </span>
                              </div>
                            </TableCell>
                            <TableCell>
                              <Badge className={`${getStatusColor(buyer.status)} text-white`}>
                                {buyer.status}
                              </Badge>
                            </TableCell>
                            <TableCell>
                              <div className="flex gap-2">
                                <Button size="sm" variant="outline">
                                  <Eye className="w-4 h-4" />
                                </Button>
                                <Button size="sm">
                                  <ExternalLink className="w-4 h-4" />
                                </Button>
                              </div>
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </TabsContent>

                  {/* Detailed View */}
                  <TabsContent value="detailed" className="space-y-6 mt-0">
                    {mockResearchResult.discoveredBuyers.map((buyer) => (
                      <Card key={buyer.id} className="border-border">
                        <CardHeader>
                          <div className="flex items-start justify-between">
                            <div>
                              <h3 className="text-lg font-semibold text-foreground">{buyer.name}</h3>
                              <div className="flex items-center gap-4 mt-1">
                                <div className="flex items-center gap-1">
                                  <MapPin className="w-4 h-4 text-muted-foreground" />
                                  <span className="text-sm text-muted-foreground">{buyer.country} • {buyer.region}</span>
                                </div>
                                <div className="flex items-center gap-1">
                                  <Globe className="w-4 h-4 text-muted-foreground" />
                                  <a href={buyer.website} target="_blank" rel="noopener noreferrer" 
                                     className="text-sm text-primary hover:underline">
                                    {buyer.website}
                                  </a>
                                </div>
                              </div>
                            </div>
                            <div className="flex items-center gap-3">
                              <div className="flex items-center gap-1">
                                <Star className={`w-5 h-5 ${getOpportunityScoreColor(buyer.opportunityScore)}`} />
                                <span className={`text-lg font-bold ${getOpportunityScoreColor(buyer.opportunityScore)}`}>
                                  {buyer.opportunityScore}
                                </span>
                              </div>
                              <Badge className={`${getStatusColor(buyer.status)} text-white`}>
                                {buyer.status}
                              </Badge>
                            </div>
                          </div>
                        </CardHeader>
                        <CardContent className="space-y-4">
                          <div>
                            <h4 className="font-medium text-foreground mb-2">Target Segment</h4>
                            <p className="text-sm text-muted-foreground">{buyer.targetSegment}</p>
                          </div>

                          <div>
                            <h4 className="font-medium text-foreground mb-2">Key Contacts</h4>
                            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                              {buyer.keyContacts.map((contact, idx) => (
                                <div key={idx} className="border border-border rounded-lg p-3">
                                  <div className="font-medium text-sm">{contact.name}</div>
                                  <div className="text-xs text-muted-foreground">{contact.role}</div>
                                  {contact.email && (
                                    <div className="text-xs text-primary mt-1">{contact.email}</div>
                                  )}
                                </div>
                              ))}
                            </div>
                          </div>

                          <div>
                            <h4 className="font-medium text-foreground mb-2">Recommendation Rationale</h4>
                            <p className="text-sm text-muted-foreground leading-relaxed">{buyer.reasonForRecommendation}</p>
                          </div>

                          <div className="flex gap-3 pt-2">
                            <Button className="gap-2">
                              <MessageCircle className="w-4 h-4" />
                              Generate Outreach
                            </Button>
                            <Button variant="outline" className="gap-2">
                              <Eye className="w-4 h-4" />
                              View Full Profile
                            </Button>
                            <Button variant="outline" className="gap-2">
                              <ExternalLink className="w-4 h-4" />
                              Visit Website
                            </Button>
                          </div>
                        </CardContent>
                      </Card>
                    ))}
                  </TabsContent>
                </Tabs>
              </CardContent>
            </Card>
          </>
        )}
      </main>
    </div>
  );
};

export default BuyerDiscovery;