package com.fakenews;
import org.springframework.beans.factory.annotation.Value; import org.springframework.http.*; import org.springframework.web.bind.annotation.*; import org.springframework.web.client.RestClient; import org.springframework.web.client.RestClientException; import java.util.*;
@RestController @RequestMapping("/api")
@CrossOrigin(origins={"http://localhost:5173","http://127.0.0.1:5173"})
public class ApiController {
 private final AnalysisRepository repo; private final RestClient ml;
 public ApiController(AnalysisRepository r,@Value("${ml.service.url}") String url){repo=r;ml=RestClient.builder().baseUrl(url).build();}
 @GetMapping("/health") public Map<String,String> health(){return Map.of("status","ok");}
 @GetMapping("/history") public List<Analysis> history(){return repo.findTop20ByOrderByCreatedAtDesc();}
 @PostMapping("/analyze") public ResponseEntity<?> analyze(@RequestBody Map<String,String> body){
  String text=body.get("text"); if(text==null||text.isBlank())return ResponseEntity.badRequest().body(Map.of("message","News text is required."));
  if(text.length()>20000)return ResponseEntity.badRequest().body(Map.of("message","Text must be 20,000 characters or fewer."));
  try { Map<?,?> pred=ml.post().uri("/predict").contentType(MediaType.APPLICATION_JSON).body(Map.of("text",text.trim())).retrieve().body(Map.class);
   if(pred==null)return ResponseEntity.status(502).body(Map.of("message","Empty ML response."));
   String label=String.valueOf(pred.get("prediction")); double score=((Number)pred.get("confidence")).doubleValue();
   Analysis saved=repo.save(new Analysis(text.trim(),label,score));
   Map<String,Object> out=new LinkedHashMap<>();out.put("id",saved.getId());out.put("newsText",saved.getNewsText());out.put("prediction",label);out.put("label",pred.get("label"));out.put("confidence",score);out.put("disclaimer",pred.get("disclaimer"));out.put("createdAt",saved.getCreatedAt().toString());
   return ResponseEntity.ok(out);
  } catch(RestClientException ex){return ResponseEntity.status(502).body(Map.of("message","Cannot reach ML service. Start FastAPI on port 8000."));}
 }
}
