import { AlertTriangle, CheckCircle, Clock, FileText, Shield, TrendingUp, Download, Eye, Bell } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { Alert, AlertDescription } from "@/components/ui/alert";

const mockCompliance = [
  {
    id: 1,
    regulation: "FDA 21 CFR Part 820",
    category: "Quality Management",
    status: "Compliant",
    lastAudit: "Jan 15, 2024",
    nextReview: "Jul 15, 2024",
    riskLevel: "Low",
    complianceScore: 95,
    requirements: 45,
    completed: 43,
    alerts: 0
  },
  {
    id: 2,
    regulation: "EU MDR 2017/745",
    category: "Medical Devices",
    status: "Action Required",
    lastAudit: "Dec 10, 2023",
    nextReview: "Mar 10, 2024",
    riskLevel: "Medium",
    complianceScore: 78,
    requirements: 38,
    completed: 30,
    alerts: 3
  },
  {
    id: 3,
    regulation: "ICH E6 GCP Guidelines",
    category: "Clinical Trials",
    status: "Under Review",
    lastAudit: "Feb 28, 2024",
    nextReview: "May 28, 2024",
    riskLevel: "Low",
    complianceScore: 88,
    requirements: 52,
    completed: 46,
    alerts: 1
  },
  {
    id: 4,
    regulation: "GDPR Article 9",
    category: "Data Protection",
    status: "Critical",
    lastAudit: "Nov 20, 2023",
    nextReview: "Overdue",
    riskLevel: "High",
    complianceScore: 62,
    requirements: 28,
    completed: 17,
    alerts: 5
  }
];

const recentAlerts = [
  {
    id: 1,
    type: "Critical",
    message: "GDPR compliance assessment overdue - immediate action required",
    regulation: "GDPR Article 9",
    timestamp: "2 hours ago",
    severity: "high"
  },
  {
    id: 2,
    type: "Warning",
    message: "EU MDR documentation review deadline approaching",
    regulation: "EU MDR 2017/745",
    timestamp: "1 day ago",
    severity: "medium"
  },
  {
    id: 3,
    type: "Info",
    message: "New FDA guidance document published for review",
    regulation: "FDA 21 CFR Part 820",
    timestamp: "3 days ago",
    severity: "low"
  }
];

const ComplianceMonitoring = () => {
  const getStatusColor = (status: string) => {
    switch (status) {
      case "Compliant": return "bg-gradient-success";
      case "Action Required": return "bg-warning";
      case "Under Review": return "bg-primary";
      case "Critical": return "bg-destructive";
      default: return "bg-muted";
    }
  };

  const getRiskColor = (risk: string) => {
    switch (risk) {
      case "Low": return "text-success";
      case "Medium": return "text-warning";
      case "High": return "text-destructive";
      default: return "text-muted-foreground";
    }
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-gradient-card shadow-card">
        <div className="flex h-16 items-center justify-between px-6">
          <div className="flex items-center gap-6">
            <h1 className="text-xl font-bold text-foreground">Compliance Monitoring</h1>
          </div>
          <div className="flex items-center gap-3">
            <Button variant="outline" size="sm" className="gap-2">
              <Download className="w-4 h-4" />
              Export Report
            </Button>
            <Button variant="outline" size="sm" className="gap-2">
              <Bell className="w-4 h-4" />
              Alert Settings
            </Button>
            <Button className="gap-2">
              <FileText className="w-4 h-4" />
              Generate Report
            </Button>
          </div>
        </div>
      </header>

      <main className="p-6 space-y-6">
        {/* Overview Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <Card className="bg-gradient-card border-border">
            <CardContent className="p-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-gradient-primary rounded-lg flex items-center justify-center">
                  <Shield className="w-5 h-5 text-primary-foreground" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Total Regulations</p>
                  <p className="text-2xl font-bold text-foreground">847</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-card border-border">
            <CardContent className="p-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-gradient-success rounded-lg flex items-center justify-center">
                  <CheckCircle className="w-5 h-5 text-success-foreground" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Compliant</p>
                  <p className="text-2xl font-bold text-foreground">789</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-card border-border">
            <CardContent className="p-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-warning/20 rounded-lg flex items-center justify-center">
                  <AlertTriangle className="w-5 h-5 text-warning" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Action Required</p>
                  <p className="text-2xl font-bold text-foreground">23</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-card border-border">
            <CardContent className="p-4">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-destructive/20 rounded-lg flex items-center justify-center">
                  <Clock className="w-5 h-5 text-destructive" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Overdue</p>
                  <p className="text-2xl font-bold text-foreground">8</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Recent Alerts */}
        <Card className="bg-gradient-card border-border">
          <CardHeader>
            <CardTitle className="text-foreground flex items-center gap-2">
              <Bell className="w-5 h-5" />
              Recent Compliance Alerts
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {recentAlerts.map((alert) => (
                <Alert key={alert.id} className={`border-l-4 ${
                  alert.severity === 'high' ? 'border-l-destructive' :
                  alert.severity === 'medium' ? 'border-l-warning' : 'border-l-primary'
                }`}>
                  <AlertTriangle className="h-4 w-4" />
                  <AlertDescription>
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <div className="flex items-center gap-2 mb-1">
                          <Badge variant={alert.severity === 'high' ? 'destructive' : 
                                        alert.severity === 'medium' ? 'default' : 'secondary'}>
                            {alert.type}
                          </Badge>
                          <span className="text-xs text-muted-foreground">{alert.timestamp}</span>
                        </div>
                        <p className="text-sm font-medium text-foreground mb-1">{alert.message}</p>
                        <p className="text-xs text-muted-foreground">Regulation: {alert.regulation}</p>
                      </div>
                      <Button variant="outline" size="sm">
                        Review
                      </Button>
                    </div>
                  </AlertDescription>
                </Alert>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Compliance Dashboard */}
        <Card className="bg-gradient-card border-border">
          <CardHeader>
            <CardTitle className="text-foreground">Compliance Status Dashboard</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-6">
              {mockCompliance.map((item) => (
                <div key={item.id} className="border border-border rounded-lg p-4">
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <h3 className="font-semibold text-foreground text-lg">{item.regulation}</h3>
                        <Badge className={getStatusColor(item.status)}>
                          {item.status}
                        </Badge>
                        <span className={`text-sm font-medium ${getRiskColor(item.riskLevel)}`}>
                          {item.riskLevel} Risk
                        </span>
                        {item.alerts > 0 && (
                          <Badge variant="destructive" className="ml-auto">
                            {item.alerts} Alert{item.alerts > 1 ? 's' : ''}
                          </Badge>
                        )}
                      </div>
                      
                      <p className="text-sm text-muted-foreground mb-3">{item.category}</p>
                      
                      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-4">
                        <div>
                          <span className="text-xs text-muted-foreground">Last Audit: </span>
                          <span className="text-xs font-medium text-foreground">{item.lastAudit}</span>
                        </div>
                        <div>
                          <span className="text-xs text-muted-foreground">Next Review: </span>
                          <span className={`text-xs font-medium ${item.nextReview === 'Overdue' ? 'text-destructive' : 'text-foreground'}`}>
                            {item.nextReview}
                          </span>
                        </div>
                        <div>
                          <span className="text-xs text-muted-foreground">Requirements: </span>
                          <span className="text-xs font-medium text-foreground">
                            {item.completed}/{item.requirements}
                          </span>
                        </div>
                        <div>
                          <span className="text-xs text-muted-foreground">Score: </span>
                          <span className="text-xs font-medium text-foreground">{item.complianceScore}%</span>
                        </div>
                      </div>

                      <div className="space-y-2">
                        <div className="flex items-center justify-between">
                          <span className="text-xs text-muted-foreground">Compliance Progress</span>
                          <span className="text-xs text-foreground">{item.complianceScore}%</span>
                        </div>
                        <Progress 
                          value={item.complianceScore} 
                          className="h-2"
                        />
                      </div>
                    </div>

                    <div className="flex flex-col gap-2 ml-4">
                      <Button size="sm" className="gap-2">
                        <Eye className="w-4 h-4" />
                        Details
                      </Button>
                      <Button variant="outline" size="sm" className="gap-2">
                        <FileText className="w-4 h-4" />
                        Documents
                      </Button>
                      {item.alerts > 0 && (
                        <Button variant="destructive" size="sm" className="gap-2">
                          <AlertTriangle className="w-4 h-4" />
                          Review Alerts
                        </Button>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Compliance Trends */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <Card className="bg-gradient-card border-border">
            <CardHeader>
              <CardTitle className="text-foreground flex items-center gap-2">
                <TrendingUp className="w-5 h-5" />
                Compliance Score Trends
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="flex items-center justify-between p-3 border border-border rounded-lg">
                  <div>
                    <p className="text-sm font-medium text-foreground">Overall Score</p>
                    <p className="text-xs text-muted-foreground">Last 30 days</p>
                  </div>
                  <div className="text-right">
                    <p className="text-lg font-bold text-success">+5.2%</p>
                    <p className="text-xs text-muted-foreground">Improved</p>
                  </div>
                </div>
                <div className="flex items-center justify-between p-3 border border-border rounded-lg">
                  <div>
                    <p className="text-sm font-medium text-foreground">Critical Issues</p>
                    <p className="text-xs text-muted-foreground">Last 30 days</p>
                  </div>
                  <div className="text-right">
                    <p className="text-lg font-bold text-destructive">-23%</p>
                    <p className="text-xs text-muted-foreground">Reduced</p>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-card border-border">
            <CardHeader>
              <CardTitle className="text-foreground">Upcoming Reviews</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                <div className="flex items-center justify-between p-3 border border-border rounded-lg">
                  <div>
                    <p className="text-sm font-medium text-foreground">EU MDR 2017/745</p>
                    <p className="text-xs text-muted-foreground">Medical Devices</p>
                  </div>
                  <div className="text-right">
                    <p className="text-sm font-medium text-warning">Mar 10, 2024</p>
                    <p className="text-xs text-muted-foreground">2 weeks</p>
                  </div>
                </div>
                <div className="flex items-center justify-between p-3 border border-border rounded-lg">
                  <div>
                    <p className="text-sm font-medium text-foreground">ICH E6 GCP Guidelines</p>
                    <p className="text-xs text-muted-foreground">Clinical Trials</p>
                  </div>
                  <div className="text-right">
                    <p className="text-sm font-medium text-foreground">May 28, 2024</p>
                    <p className="text-xs text-muted-foreground">3 months</p>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  );
};

export default ComplianceMonitoring;