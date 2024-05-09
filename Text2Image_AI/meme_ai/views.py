from django.shortcuts import render
import torch
from diffusers import AutoPipelineForText2Image, DEISMultistepScheduler
# Create your views here.
from django.views import View


class ClassAI(View):
    def post(self, request):
        styles_obj = request.data
        styles = styles_obj.get('styles')
        prompt = styles_obj.get('prompt')
        pipe = AutoPipelineForText2Image.from_pretrained('lykon/dreamshaper-8', torch_dtype=torch.float16,
                                                         variant="fp16")
        pipe.scheduler = DEISMultistepScheduler.from_config(pipe.scheduler.config)
        pipe = pipe.to("cuda")
        styles = styles
        promt = prompt
        prompt_1 = "generate a " + styles + "art that's" + prompt
        generator = torch.manual_seed(33)
        image = pipe(prompt_1, generator=generator, num_inference_steps=50).images[0]
        image.save("./image.png")
        context = {'image_url': '/static/image.png'}  # Update the URL as per your project structure

        return render(request, 'your_template.html', context)

# Create your views here.
